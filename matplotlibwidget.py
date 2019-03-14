import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QFrame, QGridLayout
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from matplotlib.animation import TimedAnimation
from matplotlib.lines import Line2D
import time
import threading

import numpy as np
from sensors import *


class Communicate(QtCore.QObject):
    data_signal = QtCore.pyqtSignal(list)

class SensorsMatplotlibQWidget(FigureCanvas, TimedAnimation):
    def __init__(self):
        self.n = np.linspace(0, 1, 1)
        self.abc = 1
        self.sensors = Sensors()
        self.sensors_port = self.sensors.port
        self.sensors.flush()

        self.temp_yar = [0]
        self.humidity_yar = [0]
        self.smoke_conc = [0]
        self.time_ar = [0]

        self.current_temp_1 = 0
        self.current_temp_2 = 0
        self.current_hum_1 = 0
        self.current_hum_2 = 0
        self.current_smoke_concentration = 0

        # Set up figure
        self.fig = Figure(figsize=(4,12), dpi=80)
        self.fig.suptitle("Sensor Data")
        self.fig.subplots_adjust(wspace=0.4)

        FigureCanvas.__init__(self, self.fig)
        TimedAnimation.__init__(self, self.fig, interval = 2000, blit = True)

    def new_frame_seq(self):
        return iter(range(self.n.size))

    def _init_draw(self):
        temp_low, temp_high = self.sensors.get_temp_limits()
        humidity_low, humidity_high = self.sensors.get_humidity_limits()
        gas_conc_low, gas_conc_high = self.sensors.get_gas_conc_limits()

        # Mean Temperature Plot
        self.temp_ax = self.fig.add_subplot(3, 1, 1)
        self.temp_ax.set_ylim(temp_low, temp_high)
        self.temp_line, = self.temp_ax.plot(self.time_ar, self.temp_yar, 'g', marker='^')

        # Mean Humidity Plot
        self.humidity_ax = self.fig.add_subplot(3, 1, 2)
        self.humidity_ax.set_ylim(humidity_low, humidity_high)
        self.humidity_line, = self.humidity_ax.plot(self.time_ar, self.humidity_yar, 'b', marker='^')

        # Smoke Concentration
        self.gas_conc_ax = self.fig.add_subplot(3, 1, 3)
        self.gas_conc_ax.set_ylim(gas_conc_low, gas_conc_high)
        self.gas_conc_line, = self.gas_conc_ax.plot(self.time_ar, self.smoke_conc, 'r', marker='^')

    def addData(self, value):
        self.time_ar.append(self.time_ar[-1] + 2)
        self.current_smoke_concentration, self.current_temp_1, self.current_temp_2, max_temp, self.current_hum_1, self.current_hum_2 = value
        self.current_smoke_concentration = float(self.current_smoke_concentration)
        self.current_temp_1 = float(self.current_temp_1)
        self.current_temp_2 = float(self.current_temp_2)
        max_temp = float(max_temp)
        self.current_hum_1 = float(self.current_hum_1)
        self.current_hum_2 = float(self.current_hum_2)

        self.temp_yar.append((self.current_temp_1 + float(self.current_temp_2))/2)
        self.humidity_yar.append((self.current_hum_1 + self.current_hum_2)/2)
        self.smoke_conc.append(self.current_smoke_concentration)

    def addData_callbackFunc(self, value):
        self.addData(value)

    def _step(self, *args):
        try:
            TimedAnimation._step(self, *args)
        except Exception:
            self.abc += 1
            print(str(self.abc))
            TimedAnimation._stop(self)

    def _draw_frame(self, framedata):
        self.temp_line.set_data(self.time_ar, self.temp_yar)
        self.humidity_line.set_data(self.time_ar, self.humidity_yar)

        time_min = self.time_ar[-1] - 10
        time_max = time_min + 11
        self.temp_ax.set_xlim(time_min, time_max)
        self.humidity_ax.set_xlim(time_min, time_max)

        self.temp_ax.set_xticks(np.arange(time_min, time_max, 2))
        self.humidity_ax.set_xticks(np.arange(time_min, time_max, 2))
        if(len(self.time_ar) > 13):
            self.time_ar.pop(0)
            self.temp_yar.pop(0)
            self.humidity_yar.pop(0)

    def dataSendLoop(self, addData_callbackFunc):
        # Setup the signal-slot mechanism.
        mySrc = Communicate()
        mySrc.data_signal.connect(addData_callbackFunc)

        while(True):
            if self.sensors_port != self.sensors.get_port():
                break
            time.sleep(2)
            mySrc.data_signal.emit(self.sensors.get_data()) # <- Here you emit a signal!

    def stop(self):
        self.stop_event_loop()
