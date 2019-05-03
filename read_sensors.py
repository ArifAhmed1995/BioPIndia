import sys
import serial

# This is meant to be a runnable script. So, no OOP unless you know what you're doing :)

#sensors = serial.Serial(port=sys.argv[1], baudrate=int(sys.argv[2]))

# This flips out for some reason :(

while True:# Because sensors read continuously till application terminates.
    #   sensor_data = sensors.readline()
    sensor_data = "20 20 20 20 20 20"
    print(sensor_data)

