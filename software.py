import os
import sys
import subprocess
import threading

from biopindia import Ui_BioPIndia

from serial import SerialException

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLCDNumber, QMessageBox, QFileDialog, QGridLayout


from matplotlibwidget import SensorsMatplotlibQWidget
from webcam import *

class BioPIndiaApp(QtWidgets.QMainWindow, Ui_BioPIndia):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_BioPIndia.__init__(self)
        self.setupUi(self)

        self.stl_file = None
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

        # Exit choice on menu bar
        self.actionExit.triggered.connect(self.exit)

        # Live Plot for sensors
        self.gridLayout = QGridLayout()
        self.sensors_plot_widget = SensorsMatplotlibQWidget()
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

        lcd_thread = threading.Thread(name = 'LCD_Thread',
                    target = self.update_sensor_lcds, daemon = True)
        lcd_thread.start()


        # Webcam Widget Integration
        self.webcam_widget = WebcamQWidget()
        self.webcam_grid.addWidget(self.webcam_widget.get(), *(0,1))

        # Menu Bar handlers
        self.actionCOM.triggered.connect(lambda : self.switch_COM("/dev/ttyUSB0"))
        self.actionCOM2.triggered.connect(lambda : self.switch_COM("/dev/ttyUSB1"))
        self.actionCOM3.triggered.connect(lambda : self.switch_COM("/dev/ttyACM0"))
        self.actionGenerate_GCode_for_STL_File.triggered.connect(self.generate_gcode)
        #self.actionPost_process_GCode_for_BioP.triggered.connect(self.post_process())
        self.actionPrint_via_RepetierHost.triggered.connect(self.open_repetier_host)
        self.actionView_Loaded_STL_File.triggered.connect(self.view_stl_file)
        self.actionLoad_STL_File.triggered.connect(self.load_stl_file)

    def addSensorsMatplotlibQWidget(self, sensors_plot_widget):
        self.gridLayout.addWidget(sensors_plot_widget, *(0,1))

        self.sensors_plot_thread = threading.Thread(name = 'Sensors_Plot_Thread',
                    target = sensors_plot_widget.dataSendLoop,
                    daemon = True, args = (sensors_plot_widget.addData_callbackFunc,))
        self.sensors_plot_thread.start()

    def update_sensor_lcds(self):
        while(True):
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
            fstl = self.current_dir + "/fstl/build/fstl " + str(self.stl_file)
            subprocess.Popen(fstl, shell=True)

    def generate_gcode(self):
        if self.stl_found():
            generate_command = "slic3r " + str(self.stl_file) +" --output output.gcode"
            subprocess.Popen(generate_command, shell=True)
            return self.current_dir + "/output.gcode"

    def open_repetier_host(self):
        subprocess.check_call("./Repetier-Host-x86_64-2.1.2.AppImage",
            stdout=subprocess.PIPE, shell=True)

    def load_stl_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.stl_file, _ = QFileDialog.getOpenFileName(self,"Select a STL File", "",
                                                "STL Files (*.stl *.STL)",options=options)

    def switch_COM(self, port):
        #try:
        self.dht11_plot_widget.dht11_sensor.set_port(port)
        self.addDHT11MatplotlibQWidget(self.dht11_plot_widget)
        #except SerialException:
        #    QMessageBox().critical(self, "Port Access Error", "Could not open port "+port, QMessageBox.Ok)

    def exit(self):
        quit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    bioapp = BioPIndiaApp()
    bioapp.show()
    sys.exit(app.exec_())
