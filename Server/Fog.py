import random

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'
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
        if result == None:
            data[topic[2]] = [msg.payload.decode(), ""]
        else:
            result[0] = msg.payload.decode()

    elif topic[1] == "queue":
        if result != None:
            result[1] = msg.payload.decode()
        else:
            data[topic[2]] = ["", msg.payload.decode()]
    
        


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
