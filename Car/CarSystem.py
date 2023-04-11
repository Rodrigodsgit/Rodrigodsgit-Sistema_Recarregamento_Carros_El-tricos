import random
from geopy.distance import geodesic
import json
from flask import Flask, request
import threading
from Car import Car
import time

app = Flask(__name__)
alert = False
car = Car(random.uniform(-12.285, -12.205), random.uniform(-38.990, -38.905))
stations = [
    ("localhost", 5000, (-12.240, -38.950)),
    ("localhost", 5001, (-12.245, -38.950)),
    ("localhost", 5002, (-12.245, -38.970))
]
nearestStation = None
lockNearestStation = threading.Lock()

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
    global nearestStation 
    nearestStation = findStation

def infoAlert():
    lockNearestStation.acquire()
    response = request.get(f'http://{nearestStation[0]}:{nearestStation[1]}/lessQueue')
    lockNearestStation.release()
    if 200 <= response.status_code < 300:
        idStation, station = response.json().popitem()
        print(f"Bateria baixa")
        print(f"Va para o posto {idStation}")
    else:
        print(f"Erro {response.status_code} ao se conectar ao servidor {nearestStation[0]}:{nearestStation[1]}")

def avaliableBattery(car):
    while (True):
        if car.isLowBattery(car) and not alert:
            alert = True
            infoAlert(nearestStation(car))
        else:
            alert = False

def printCarBattery(car):
    while (True):
        time.sleep(10)
        print(f"Baterria em {car.battery}%")

def main(car):
    printCarBatteryThread = threading.Thread(target=printCarBattery, args=(car,)) 
    consumeBetteryThread = threading.Thread(target=consumeBattery, args=(car,))
    avaliableBatteryThread = threading.Thread(target=avaliableBattery, args=(car,))

    consumeBetteryThread.start()
    avaliableBatteryThread.start()
    printCarBatteryThread.start()

    printCarBatteryThread.join()
    consumeBetteryThread.join()
    avaliableBatteryThread.join()
    return

if __name__ == '__main__':
    main(car)
