
import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'
latitude = 0
longitude = 0
coordinates = f"{latitude}/{longitude}"


def connect_mqtt():
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


def publish(client):
    client.publish(f"station/map/{client_id}",coordinates)
    while True:
        time.sleep(10)
        topic = f"station/queue/{client_id}"
        msg = random.randint(0,10)
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


def menu():
    while True:
        latitude = float(input("Enter your latitude coordinate: "))  
        longitude = float(input("Enter your longitude coordinate: "))
        if (-12.205 >= latitude >= -12.285) and (-38.905 >= longitude >= -38.990):
            print("Established geographical area")
            break
        else:
            print("Out of area")




def run():
    menu()
    client = connect_mqtt()
    client.loop_start()
    publish(client)



if __name__ == '__main__':
    run()
