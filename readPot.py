from nanpy import (Servo, ArduinoApi, SerialManager)

potPin = 0

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")

a.pinMode(potPin, a.INPUT)

def readPot():
    val = a.analogRead(potPin)
    print("Analog value of potentiometer is: ", val)
    return val
