import random
import json
from flask import Flask, request
import threading
from Car import Car
import time

app = Flask(__name__)
ip = "localhost"
port = 5000
car = Car(random.uniform(-12.285, -12.205), random.uniform(-38.990, -38.905))
car.upBatteryConsumption()

def consumeBattery(car : Car):
    while (True):
        time.sleep(5)
        car.consumeBattery()

#a terminar
def alert():
    time.sleep(3)
    print("Bateria baixa")

def avaliableBattery(car : Car):
    while (True):
        if car.battery < 30:
            alert()

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