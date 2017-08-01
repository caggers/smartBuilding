from nanpy import (Servo, ArduinoApi, SerialManager)
from time import sleep
from readPot import readPot

ledPin = 6
ledState = False


try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")


a.pinMode(ledPin, a.OUTPUT)

try:
    while True:
        potVal = readPot()
        writeVal = (255./1023.) * potVal
        a.analogWrite(ledPin, writeVal)
        print("The write val is: ", writeVal)


except:
    a.digitalWrite(ledPin, a.LOW)
