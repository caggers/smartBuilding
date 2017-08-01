from nanpy import (ArduinoApi, SerialManager)
from time import sleep
from readButton import readButton

ledPin = 7
ledState = False

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")


a.pinMode(ledPin, a.OUTPUT)

try:
    while True:
        buttonState = readButton()
        if buttonState:
            if ledState:
                a.digitalWrite(ledPin, a.LOW)
                ledState = False
                print("LED OFF")
                sleep(1)
            else:
                a.digitalWrite(ledPin, a.HIGH)
                ledState = True
                print("LED ON")
                sleep(1)

except:
    a.digitalWrite(ledPin, a.LOW)
                    
