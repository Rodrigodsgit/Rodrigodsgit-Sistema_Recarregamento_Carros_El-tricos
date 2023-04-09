import random

from paho.mqtt import client as mqtt_client
from flask import Flask
from geopy.distance import geodesic
import threading

broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'
latitude = -12.240
longitude = -38.950
data = {}


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
    result = data.get(topic[2])

    if topic[1] == "map":
        coordinates = msg.payload.decode().split("/")
        if result == None:
            latitude = float(coordinates[0])
            longitude = float(coordinates[1])
            data[topic[2]] = [latitude, longitude, ""]
        else:
            result[0] = round(coordinates[0],3)
            result[1] =round(coordinates[1],3)

    elif topic[1] == "queue":
        if result != None:
            result[2] = msg.payload.decode()
        else:
            data[topic[2]] = ["","", msg.payload.decode()]
    
    print(data)

    
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


app = Flask(__name__)

@app.route('/lessQueue', methods=['GET'])
def less_queue():
    # bestStation = 0

    # for id, info in data:
    #     coord1 = (latitude, longitude)
    #     coord2 = (info[0], -38.990)

    #     dist = geodesic(coord1, coord2).km
    #     dist = round(dist,2)
    return "Teste"

if __name__ == '__main__':
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=app.run)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    