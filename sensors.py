import os
import re
import threading
import serial
import time

import numpy as np

from port_methods import get_arduino_port

class Sensors:
    def __init__(self, baudrate = 9600):
        self.port = get_arduino_port()
        self.baudrate = baudrate

        self.sensors = serial.Serial(self.port, baudrate=self.baudrate,
                                  bytesize=serial.EIGHTBITS,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE,
                                  timeout=2, xonxoff=0, rtscts=0)

        self.active = self.sensors.isOpen()
        self.time_ar = []
        self.temp_yar = []
        self.humidity_yar = []

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port

    def is_active(self):
        return self.active

    def flush(self):
        # Flush the port
        self.sensors.readline()

    def get_data(self):
        while(self.sensors.inWaiting()==0):
            pass
        return self.sensors.readline().split()

    def get_temp_limits(self):
        return 20, 70

    def get_humidity_limits(self):
        return 40, 100

    def get_gas_conc_limits(self):
        return 0, 200

    def plot_data(self, figure):
        self.flush()

        temp_low, temp_high = self.get_temp_limits()
        humidity_low, humidity_high = self.get_humidity_limits()

        self.temp_ax = figure.add_subplot(2, 2, 1)
        self.temp_ax.set_ylim(temp_low, temp_high)
        self.temp_line, = self.temp_ax.plot(self.time_ar, self.temp_yar, 'g', marker='x')

        self.humidity_ax = figure.add_subplot(2, 2, 2)
        self.humidity_ax.set_ylim(humidity_low, humidity_high)
        self.humidity_line, = self.humidity_ax.plot(self.time_ar, self.humidity_yar, 'b', marker='x')

    def update_dht11(self, i):
        sensor_data = self.get_data()

        self.temp_yar.append(float(sensor_data[0]))
        self.humidity_yar.append(float(sensor_data[1]))

        self.time_ar.append(i)
        self.temp_line.set_data(self.time_ar, self.temp_yar)
        self.humidity_line.set_data(self.time_ar, self.humidity_yar)

        self.temp_ax.set_xlim(i-10, i+1)
        self.humidity_ax.set_xlim(i-10, i+1)

        if(len(self.time_ar) > 15):
            self.time_ar.pop(0)
            self.temp_yar.pop(0)
            self.humidity_yar.pop(0)

        print(self.port)
