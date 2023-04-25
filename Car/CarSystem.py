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
stations = [
    ("localhost", 5000, (-12.240, -38.950)),
    ("localhost", 5000, (-12.245, -38.950)),
    ("localhost", 5000, (-12.245, -38.970))
]

car.upBatteryConsumption()

def consumeBattery(car):
    while (True):
        time.sleep(5)
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

def avaliableBattery(car):
    while (True):
        if car.isLowBattery() and not alert:
            alert = True
            infoAlert(findNearestStation(car), car)
        elif not car.isLowBattery():
            alert = False

def carInMoviment(car):
    car.setVelocity(random.randint(20, 80))
    print(f"O carro esta a {car.velocity} km/h")

    while (True):
        destiny = [random.uniform(-12.285, -12.205), random.uniform(-38.990, -38.905)]
        print(f"Indo para {destiny}")
        while (car.latitude != destiny[0] and car.longitude != destiny[1]):
            time.sleep(10)
            car.updateLocation(1,destiny)
            print(f"Carro esta em [{car.latitude},{car.longitude}]")

def printCarBattery(car):
    while (True):
        time.sleep(10)
        print(f"Baterria em {car.battery}%")

def main(car):

    printCarBatteryThread = threading.Thread(target=printCarBattery, args=(car,)) 
    consumeBetteryThread = threading.Thread(target=consumeBattery, args=(car,))
    avaliableBatteryThread = threading.Thread(target=avaliableBattery, args=(car,))
    carInMovimentThread = threading.Thread(target=carInMoviment, args=(car,))

    consumeBetteryThread.start()
    avaliableBatteryThread.start()
    printCarBatteryThread.start()
    carInMovimentThread.start()

    printCarBatteryThread.join()
    consumeBetteryThread.join()
    avaliableBatteryThread.join()
    carInMovimentThread.join()
    return

if __name__ == '__main__':
    main(car)
