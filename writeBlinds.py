from nanpy import (Servo, ArduinoApi, SerialManager)
from helpers import my_map
from readPot import readPot

servo = Servo(9)
servo.write(0)


try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")

try:
    while True:
        potVal = readPot()
        val = my_map(potVal, 0, 1023, 0, 179)
        print("The servo value is: ", val)
        servo.write(val)

except:
    servo.write(0)
