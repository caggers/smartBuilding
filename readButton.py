from nanpy import (ArduinoApi, SerialManager)

buttonPin = 8
buttonState = 0

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")


a.pinMode(buttonPin, a.INPUT)

def readButton():
    buttonState = a.digitalRead(buttonPin)
    print("Button state is: {}".format(buttonState))
    return buttonState
