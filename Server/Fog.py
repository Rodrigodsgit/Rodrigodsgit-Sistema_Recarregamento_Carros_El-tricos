import random
import json
import threading

from paho.mqtt import client as mqtt_client
from flask import Flask, request
from geopy.distance import geodesic


broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'
backup = {}


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        msg_decode(msg)
    
    client.subscribe("station/map/+")
    client.subscribe("station/queue/+")
    client.on_message = on_message

def msg_decode(msg):
    topic = msg.topic.split("/")
    result = backup.get(topic[2])

    if topic[1] == "map":
        coordinates = msg.payload.decode().split("/")
        if result == None:
            latitude = float(coordinates[0])
            longitude = float(coordinates[1])
            backup[topic[2]] = [latitude, longitude, 0]
        else:
            result[0] = round(coordinates[0],3)
            result[1] =round(coordinates[1],3)

    elif topic[1] == "queue":
        if result != None:
            result[2] = msg.payload.decode()
        else:
            backup[topic[2]] = [0,0, msg.payload.decode()]
    
    print(backup)

    
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


app = Flask(__name__)

@app.route('/lessQueue', methods=['POST'])
def less_queue():
    bestStationTime = None

    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    coord1 = (latitude, longitude)
    km_hr = 60
    recharge = 25
    result = {}

    for id, info in backup.items():    

        coord2 = (info[0], info[1])
        dist = geodesic(coord1, coord2).km
        dist = round(dist,2)
        timeDist = round(dist/km_hr,2)
        timeRecharge = round(float(info[2]) * recharge,2)
        totalTime = timeDist + timeRecharge

        if bestStationTime == None:
            bestStationTime = [id, totalTime, dist, info[2]]
        else:
            if bestStationTime[1] > totalTime:
                bestStationTime = [id, totalTime, dist, info[2]]
        
    result[bestStationTime[0]] = bestStationTime[1:]
    result = json.dumps(result)
    return result

@app.route('/stations' , methods=['GET'])
def stations():
    listStation = {}
    listStation['stations'] = list(backup.keys())
    result = json.dumps(listStation)
    return result

@app.route('/allData', methods=['GET'])
def allData():
    result = json.dumps(backup)
    return result
if __name__ == '__main__':
    door = int(input("Enter the fog port: "))
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=app.run, kwargs={'port': door})

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    