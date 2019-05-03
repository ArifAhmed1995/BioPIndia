import os
import sys
import subprocess

import threading

from threading import Timer
from threading import Thread

from biopindia import Ui_BioPIndia

from serial import SerialException

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber, QApplication, QMessageBox, QFileDialog, QPlainTextEdit


from matplotlibwidget import SensorsMatplotlibQWidget
from lcd_widgets import LCDTimer
from gcode_textbox import GCodeTextBox

from webcam import *

from port_methods import PortMethods

class BioPIndiaApp(QtWidgets.QMainWindow, Ui_BioPIndia):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_BioPIndia.__init__(self)
        self.setupUi(self)

        self.stl_file = None
        self.gcode_file = None

        self.current_dir = os.getcwd()

        # Exit choice on menu bar
        self.actionExit.triggered.connect(self.exit)

        # One time port open for both sensors and extruder. This must
        # be done and one time only otherwise read/write issues will arise
        # with the activation key file.
        self.pm = PortMethods()

        # Live Plot for sensors
        self.sensors_plot_widget = SensorsMatplotlibQWidget(self.pm.get_sensors_port())
        self.addSensorsMatplotlibQWidget(self.sensors_plot_widget)

        # LCD update functions
        palette_humidity_1 = self.humidity_1_lcd.palette()
        palette_humidity_2 = self.humidity_2_lcd.palette()
        palette_temp_1 = self.temp_1_lcd.palette()
        palette_temp_2 = self.temp_2_lcd.palette()
        palette_smoke_conc = self.smoke_conc_lcd.palette()

        palette_humidity_1.setColor(palette_humidity_1.Light, QtGui.QColor(0, 95, 255))
        palette_humidity_2.setColor(palette_humidity_2.Light, QtGui.QColor(0, 95, 255))
        palette_temp_1.setColor(palette_temp_1.Light, QtGui.QColor(93, 95, 25))
        palette_temp_2.setColor(palette_temp_2.Light, QtGui.QColor(93, 95, 25))
        palette_smoke_conc.setColor(palette_smoke_conc.Light, QtGui.QColor(3, 195, 125))

        self.humidity_1_lcd.setPalette(palette_humidity_1)
        self.humidity_2_lcd.setPalette(palette_humidity_2)
        self.temp_1_lcd.setPalette(palette_temp_1)
        self.temp_2_lcd.setPalette(palette_temp_2)
        self.smoke_conc_lcd.setPalette(palette_smoke_conc)

        # Self start timer
        self.lcd_thread = LCDTimer(1 , self.update_sensor_lcds)

        # Webcam Widget Integration
        self.webcam_widget = WebcamQWidget()
        self.webcam_grid.addWidget(self.webcam_widget.get(), *(0,1))

        # Menu Bar handlers
        self.actionCOM.triggered.connect(lambda : self.switch_COM("/dev/ttyUSB0"))
        self.actionCOM2.triggered.connect(lambda : self.switch_COM("/dev/ttyUSB1"))
        self.actionCOM3.triggered.connect(lambda : self.switch_COM("/dev/ttyACM0"))
        self.actionGenerate_GCode_for_STL_File.triggered.connect(self.generate_gcode)
        self.actionPrint_via_RepetierHost.triggered.connect(self.open_repetier_host)
        self.actionView_Loaded_STL_File.triggered.connect(self.view_stl_file)
        self.actionLoad_STL_File.triggered.connect(self.load_stl_file)
        self.actionView_Edit_GCode.triggered.connect(self.open_gcode_editor)

    def addSensorsMatplotlibQWidget(self, sensors_plot_widget):
        self.sensor_plot_grid.addWidget(sensors_plot_widget, *(0,1))

        self.sensors_plot_thread = threading.Thread(name = 'Sensors_Plot_Thread',
                    target = sensors_plot_widget.dataSendLoop,
                    daemon = True, args = (sensors_plot_widget.addData_callbackFunc,))
        self.sensors_plot_thread.start()

    def update_sensor_lcds(self):
        self.humidity_1_lcd.display(self.sensors_plot_widget.current_hum_1)
        self.humidity_2_lcd.display(self.sensors_plot_widget.current_hum_2)
        self.temp_1_lcd.display(self.sensors_plot_widget.current_temp_1)
        self.temp_2_lcd.display(self.sensors_plot_widget.current_temp_2)
        self.smoke_conc_lcd.display(self.sensors_plot_widget.current_smoke_concentration)

    def stl_found(self):
        if self.stl_file is None:
            QMessageBox().critical(self, "STL Load Error", "The STL file was not loaded", QMessageBox.Ok)
            return False
        return True

    def view_stl_file(self):
        if self.stl_found():
            fstl_path = "'" + self.current_dir + "/fstl/build/fstl" + "' '" + str(self.stl_file) + "'"
            subprocess.Popen(fstl_path, shell=True)

    def generate_gcode(self):
        if self.stl_found():
            generate_command = "slic3r " + "'" + str(self.stl_file) +"' --output output.gcode"
            subprocess.Popen(generate_command, shell=True)
            self.gcode_file = self.current_dir + "/output.gcode"

    def open_repetier_host(self):
        repetier_host_path = "'" + self.current_dir + "/RepetierHostAppImage" + "'"
        subprocess.check_call(repetier_host_path, stdout=subprocess.PIPE, shell=True)

    def load_stl_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.stl_file, _ = QFileDialog.getOpenFileName(self,"Select a STL File", "",
                                                "STL Files (*.stl *.STL)",options=options)

    def open_gcode_editor(self):
        if self.gcode_file is None:
            self.gcode_file = self.current_dir + "/output.gcode"
        self.gcode_edit_text_box = GCodeTextBox(self.gcode_file, self.pm, self.sensors_plot_widget.sensors.sensors)
        self.gcode_edit_text_box.show()

    def switch_COM(self, port):
        self.dht11_plot_widget.dht11_sensor.set_port(port)
        self.addDHT11MatplotlibQWidget(self.dht11_plot_widget)

    def exit(self):
        self.lcd_thread.terminate()
        self.sensors_plot_widget.stop()
        quit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    bioapp = BioPIndiaApp()
    bioapp.show()
    sys.exit(app.exec_())
