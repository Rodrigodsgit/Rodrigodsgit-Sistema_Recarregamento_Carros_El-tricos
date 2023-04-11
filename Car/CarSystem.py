import random
import json
from flask import Flask, request
import threading
from Car import Car
import time

app = Flask(__name__)
ip = "localhost"
port = 5000
alert = False
car = Car(random.uniform(-12.285, -12.205), random.uniform(-38.990, -38.905))
car.upBatteryConsumption()

def consumeBattery(car : Car):
    while (True):
        time.sleep(5)
        car.consumeBattery()

#a terminar
def infoAlert():
    print("Bateria baixa")

def avaliableBattery(car : Car.Car):
    while (True):
        if car.isLowBattery() and not alert:
            alert = True
            infoAlert()

def printCarBattery(car : Car):
    while (True):
        time.sleep(10)
        print(f"Baterria em {car.battery}%")

def main(car : Car):
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