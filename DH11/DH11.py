import os
import re
import threading
import serial
import time

class DH11:
    def __init__(self, port="/dev/ttyUSB0", baudrate = 9600):
        self.port = port
        self.baudrate = baudrate
        self.temperature_data = []
        self.humidity_data = []
        self.timestamp = []

        #TODO : Check if these params actually work in reality
        self.dh11 = serial.Serial(self.port, baudrate=self.baudrate,
                                  bytesize=serial.EIGHTBITS,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE,
                                  timeout=2, xonxoff=0, rtscts=0)

        #TODO : Check if 2 seconds is enough for arduino to reset
        time.sleep(2)

        self.active = self.dh11.isOpen()

    def is_active(self):
        return self.active

    def flush(self):
        # Flush the port
        self.dh11.readline()

    def get_and_plot_data(self):
        initial_timestamp = time.time()

        #Set up plot window
        plt.title("Humidity/Temperature Sensor Data")
        fig, subplt = plt.subplots(2, 1, sharex=True)
        fig.subplots_adjust(hspace=0)

        with self.dh11:
            sensor_data = re.match(r"DHT:H ([-]{0,1}\d+) T ([-]{0,1}\d+)",
                                str(self.dh11.readline()))
            if(sensor_data != None):
                self.timestamp.append(time.time()-initial_timestamp)
                self.humidity_data.append(float(int(sensor_data.group(1))/1024.0))
                self.temperature_data.append(float(int(sensor_data.group(2))/1024.0))

                subplt[0].plot(self.timestamp[1:], self.temperature_data[1:])
                subplt[0].set_yticks(np.arange(30, 40, 5))
                subplt[0].set_ylim(30, 40)
                subplt[0].set_ylabel("Temperature")
                subplt[0].set_xlabel("Time")

                subplt[1].plot(self.timestamp[1:], self.humidity_data[1:])
                subplt[1].set_yticks(np.arange(80, 95, 5))
                subplt[1].set_ylim(75, 100)
                subplt[1].set_ylabel("Humidity")
                subplt[1].set_xlabel("Time")

                plt.show(block=False)

def main():
    sensor = DH11(port="/dev/ttyUSB0", baudrate = 9600)
    sensor.flush()
    if sensor.is_active():
        sensor.get_and_plot_data()

main()
