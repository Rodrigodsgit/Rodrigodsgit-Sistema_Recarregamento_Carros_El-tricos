import random
import json
import threading
import time

from Car import Car

from geopy.distance import geodesic
from flask import Flask
import requests



app = Flask(__name__)

global alert
alert = False

car = Car(random.uniform(-12.285, -12.205), random.uniform(-38.990, -38.905))
car.upBatteryConsumption()
car.setVelocity(random.randint(20, 80))

stations = [
    ("172.16.103.7", 5001, (-12.240, -38.950)),
    ("172.16.103.7", 5002, (-12.265, -38.950)),
    ("172.16.103.7", 5003, (-12.253, -38.972))
]

def consumeBattery(car):
    while (True):
        time.sleep(5)
        if (car.getBatteryConsumption() != "off"):
            car.consumeBattery()

def findNearestStation(car):
    findStation = stations[0]
    distanceKm = geodesic(car.getCoordinates(), findStation[2]).km
    for i in stations:
        auxDistance = geodesic(car.getCoordinates(), i[2]).km
        if distanceKm > auxDistance:
            findStation = i
            distanceKm = auxDistance
    return findStation

def infoAlert(nearestStation, car):
    carCoordinates = car.getCoordinates()
    dataJson = {"latitude": carCoordinates[0], "longitude": carCoordinates[1]}
    headers = {'Content-Type': 'application/json'}
    print(dataJson)
    url = f'http://{nearestStation[0]}:{nearestStation[1]}/lessQueue'
    response = requests.post(url, headers=headers, json=dataJson)
    if 200 <= response.status_code < 300:
        idStation, station = response.json().popitem()
        print(f"Bateria baixa")
        print(f"Va para o posto {idStation} a {station[1]}")
        print(f"tem {station[2]} carros nesse posto com um tempo gasto de {station[0]}")
    else:
        print(f"Erro {response.status_code} ao se conectar ao servidor {nearestStation[0]}:{nearestStation[1]}")
    car.resetBattery()

def avaliableBattery(car):
    while (True):
        if car.isLowBattery() and not alert:
            alert = True
            infoAlert(findNearestStation(car), car)
        elif not car.isLowBattery():
            alert = False

def carInMoviment(car):
    while (True):
        destiny = [random.uniform(-12.285, -12.205), random.uniform(-38.990, -38.905)]
        print(f"Indo para [{round(destiny[0], 4)},{round(destiny[1], 4)}]")
        while (car.latitude != destiny[0] and car.longitude != destiny[1]):
            time.sleep(10)
            if (car.getBatteryConsumption() != "off"):
                car.updateLocation(0.01,destiny)
            print(f"Carro esta em [{round(car.latitude, 4)},{round(car.longitude, 4)}]")

def printCarBattery(car):
    while (True):
        time.sleep(10)
        print(f"Bateria em {car.battery}%")

def batteryConsumption(car):
    while(True):
        response = input()
        if (response == '+'):
            car.upBatteryConsumption()
            print(f"Consumo do carro modificado para {car.getBatteryConsumption()}")
        elif (response == '-'):
            car.lowerBatteryConsumption()
            print(f"Consumo do carro modificado para {car.getBatteryConsumption()}")
        else:
            print("Digite apenas + ou -")

def main(car):
    print("Carro ligado")
    print(f"Velocidade: {car.velocity} km/h")
    print(f"Consumo de Baterria: {car.getBatteryConsumption()}")
    print(f"Carro esta em [{round(car.latitude, 4)},{round(car.longitude, 4)}]")
    print("Digite '+' para aumentar o consumo de bateria")
    print("Digite '-' para reduzir o consumo de bateria")

    printCarBatteryThread = threading.Thread(target=printCarBattery, args=(car,)) 
    consumeBetteryThread = threading.Thread(target=consumeBattery, args=(car,))
    avaliableBatteryThread = threading.Thread(target=avaliableBattery, args=(car,))
    carInMovimentThread = threading.Thread(target=carInMoviment, args=(car,))
    batteryConsumptionThead = threading.Thread(target=batteryConsumption, args=(car,))

    consumeBetteryThread.start()
    avaliableBatteryThread.start()
    printCarBatteryThread.start()
    carInMovimentThread.start()
    batteryConsumptionThead.start()

    printCarBatteryThread.join()
    consumeBetteryThread.join()
    avaliableBatteryThread.join()
    carInMovimentThread.join()
    batteryConsumptionThead.join()
    return

if __name__ == '__main__':
    main(car)
