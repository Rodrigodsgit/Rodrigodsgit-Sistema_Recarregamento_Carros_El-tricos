

class Car:
    battery = 100
    batteryConsumption = 0
    #latitude = 0
    #longitude = 0
    
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def setLatitude(self, newLatitude):
        self.latitude = newLatitude

    def setLongitude(self, newLongitude):
        self.longitude = newLongitude

    def setCoordinates(self, coordinates):
        self.setLatitude(coordinates[0])
        self.setLongitude(coordinates[1])

    def getBatteryConsumption(self):
        if self.batteryConsumption == 0:
            return "off"
        elif self.batteryConsumption == 1:
            return "low"
        elif self.batteryConsumption == 2:
            return "medium"
        elif self.batteryConsumption == 3:
            return "high"
        return "erro"

    def lowerBatteryConsumption(self):
        if self.batteryConsumption > 0:
            self.batteryConsumption -= 1

    def upBatteryConsumption(self):
        if self.batteryConsumption < 3:
            self.batteryConsumption += 1

    def consumeBattery(self):
        self.battery -= 5 * self.batteryConsumption
        if self.battery < 0:
            self.battery = 0

    def resetBattery(self):
        self.battery = 100

    def isLowBattery(self) -> bool:
        if self.battery <= 20:
            return True
        return False

def printCar(car):
    print("-" * 20)
    print(f"Bateria: {testCar.battery}")
    print(f"Consumo: {testCar.getBatteryConsumption()} - {testCar.batteryConsumption}")
    print(f"Coordenadas: Lat - {testCar.latitude} | Lon - {testCar.longitude}")

if __name__ == '__main__':
    testCar = Car(10,10)


