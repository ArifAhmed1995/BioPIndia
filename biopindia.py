# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biopindia.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BioPIndia(object):
    def setupUi(self, BioPIndia):
        BioPIndia.setObjectName("BioPIndia")
        BioPIndia.resize(1154, 630)
        self.centralwidget = QtWidgets.QWidget(BioPIndia)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(710, 320, 421, 251))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.webcam_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.webcam_grid.setContentsMargins(0, 0, 0, 0)
        self.webcam_grid.setObjectName("webcam_grid")
        self.temperature_sensor_1_label = QtWidgets.QLabel(self.centralwidget)
        self.temperature_sensor_1_label.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.temperature_sensor_1_label.setObjectName("temperature_sensor_1_label")
        self.temperature_sensor_2_label = QtWidgets.QLabel(self.centralwidget)
        self.temperature_sensor_2_label.setGeometry(QtCore.QRect(20, 50, 171, 17))
        self.temperature_sensor_2_label.setObjectName("temperature_sensor_2_label")
        self.humidity_sensor_1_label = QtWidgets.QLabel(self.centralwidget)
        self.humidity_sensor_1_label.setGeometry(QtCore.QRect(20, 80, 151, 17))
        self.humidity_sensor_1_label.setObjectName("humidity_sensor_1_label")
        self.humidity_sensor_2_label = QtWidgets.QLabel(self.centralwidget)
        self.humidity_sensor_2_label.setGeometry(QtCore.QRect(20, 110, 151, 17))
        self.humidity_sensor_2_label.setObjectName("humidity_sensor_2_label")
        self.temp_1_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.temp_1_lcd.setGeometry(QtCore.QRect(215, 20, 64, 23))
        self.temp_1_lcd.setObjectName("temp_1_lcd")
        self.humidity_1_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.humidity_1_lcd.setGeometry(QtCore.QRect(215, 80, 64, 23))
        self.humidity_1_lcd.setObjectName("humidity_1_lcd")
        self.temp_2_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.temp_2_lcd.setGeometry(QtCore.QRect(215, 50, 64, 23))
        self.temp_2_lcd.setObjectName("temp_2_lcd")
        self.humidity_2_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.humidity_2_lcd.setGeometry(QtCore.QRect(215, 110, 64, 23))
        self.humidity_2_lcd.setObjectName("humidity_2_lcd")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 160, 561, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.sensor_plot_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.sensor_plot_grid.setContentsMargins(0, 0, 0, 0)
        self.sensor_plot_grid.setObjectName("sensor_plot_grid")
        self.Time_label = QtWidgets.QLabel(self.centralwidget)
        self.Time_label.setGeometry(QtCore.QRect(340, 580, 51, 17))
        self.Time_label.setObjectName("Time_label")
        self.mean_t = QtWidgets.QLabel(self.centralwidget)
        self.mean_t.setGeometry(QtCore.QRect(20, 220, 34, 16))
        self.mean_t.setObjectName("mean_t")
        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(20, 240, 91, 17))
        self.temperature.setObjectName("temperature")
        self.mean_h = QtWidgets.QLabel(self.centralwidget)
        self.mean_h.setGeometry(QtCore.QRect(20, 330, 67, 17))
        self.mean_h.setObjectName("mean_h")
        self.humidity = QtWidgets.QLabel(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(20, 350, 91, 17))
        self.humidity.setObjectName("humidity")
        self.smoke = QtWidgets.QLabel(self.centralwidget)
        self.smoke.setGeometry(QtCore.QRect(20, 440, 71, 21))
        self.smoke.setObjectName("smoke")
        self.concentration = QtWidgets.QLabel(self.centralwidget)
        self.concentration.setGeometry(QtCore.QRect(20, 460, 101, 17))
        self.concentration.setObjectName("concentration")
        self.desired_temp_label = QtWidgets.QLabel(self.centralwidget)
        self.desired_temp_label.setGeometry(QtCore.QRect(350, 20, 161, 21))
        self.desired_temp_label.setObjectName("desired_temp_label")
        self.desired_temp_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.desired_temp_spinBox.setGeometry(QtCore.QRect(490, 20, 64, 23))
        self.desired_temp_spinBox.setObjectName("desired_temp_spinBox")
        self.desired_temp_set_pushbox = QtWidgets.QPushButton(self.centralwidget)
        self.desired_temp_set_pushbox.setGeometry(QtCore.QRect(570, 17, 64, 25))
        self.desired_temp_set_pushbox.setObjectName("desired_temp_set_pushbox")
        self.stepper_speed_label = QtWidgets.QLabel(self.centralwidget)
        self.stepper_speed_label.setGeometry(QtCore.QRect(400, 80, 101, 31))
        self.stepper_speed_label.setObjectName("stepper_speed_label")
        self.mean_temp_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.mean_temp_lcd.setGeometry(QtCore.QRect(20, 260, 64, 23))
        self.mean_temp_lcd.setObjectName("mean_temp_lcd")
        self.mean_hum_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.mean_hum_lcd.setGeometry(QtCore.QRect(20, 370, 64, 23))
        self.mean_hum_lcd.setObjectName("mean_hum_lcd")
        self.smoke_conc_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.smoke_conc_lcd.setGeometry(QtCore.QRect(20, 480, 64, 23))
        self.smoke_conc_lcd.setObjectName("smoke_conc_lcd")
        self.power_off_button = QtWidgets.QPushButton(self.centralwidget)
        self.power_off_button.setGeometry(QtCore.QRect(1030, 10, 111, 31))
        self.power_off_button.setObjectName("power_off_button")
        self.stepper_speed_slider = QtWidgets.QSlider(self.centralwidget)
        self.stepper_speed_slider.setGeometry(QtCore.QRect(520, 60, 21, 81))
        self.stepper_speed_slider.setOrientation(QtCore.Qt.Vertical)
        self.stepper_speed_slider.setObjectName("stepper_speed_slider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(552, 21, 31, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(283, 80, 31, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(283, 110, 31, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(88, 370, 31, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(85, 260, 31, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(88, 480, 31, 21))
        self.label_8.setObjectName("label_8")
        BioPIndia.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BioPIndia)
        self.statusbar.setObjectName("statusbar")
        BioPIndia.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(BioPIndia)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1154, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuPort = QtWidgets.QMenu(self.menuBar)
        self.menuPort.setObjectName("menuPort")
        self.menuWebcam_Port = QtWidgets.QMenu(self.menuBar)
        self.menuWebcam_Port.setObjectName("menuWebcam_Port")
        BioPIndia.setMenuBar(self.menuBar)
        self.actionView_Loaded_STL_File = QtWidgets.QAction(BioPIndia)
        self.actionView_Loaded_STL_File.setObjectName("actionView_Loaded_STL_File")
        self.actionGenerate_GCode_for_STL_File = QtWidgets.QAction(BioPIndia)
        self.actionGenerate_GCode_for_STL_File.setObjectName("actionGenerate_GCode_for_STL_File")
        self.actionPrint_via_RepetierHost = QtWidgets.QAction(BioPIndia)
        self.actionPrint_via_RepetierHost.setObjectName("actionPrint_via_RepetierHost")
        self.actionExit = QtWidgets.QAction(BioPIndia)
        self.actionExit.setObjectName("actionExit")
        self.actionPost_process_GCode_for_BioP = QtWidgets.QAction(BioPIndia)
        self.actionPost_process_GCode_for_BioP.setObjectName("actionPost_process_GCode_for_BioP")
        self.actionCOM = QtWidgets.QAction(BioPIndia)
        self.actionCOM.setObjectName("actionCOM")
        self.actionCOM2 = QtWidgets.QAction(BioPIndia)
        self.actionCOM2.setObjectName("actionCOM2")
        self.actionCOM3 = QtWidgets.QAction(BioPIndia)
        self.actionCOM3.setObjectName("actionCOM3")
        self.actionLoad_STL_File = QtWidgets.QAction(BioPIndia)
        self.actionLoad_STL_File.setObjectName("actionLoad_STL_File")
        self.action1 = QtWidgets.QAction(BioPIndia)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(BioPIndia)
        self.action2.setObjectName("action2")
        self.menuFile.addAction(self.actionView_Loaded_STL_File)
        self.menuFile.addAction(self.actionGenerate_GCode_for_STL_File)
        self.menuFile.addAction(self.actionPrint_via_RepetierHost)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionLoad_STL_File)
        self.menuEdit.addAction(self.actionPost_process_GCode_for_BioP)
        self.menuPort.addAction(self.actionCOM)
        self.menuPort.addAction(self.actionCOM2)
        self.menuPort.addAction(self.actionCOM3)
        self.menuWebcam_Port.addAction(self.action1)
        self.menuWebcam_Port.addAction(self.action2)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuPort.menuAction())
        self.menuBar.addAction(self.menuWebcam_Port.menuAction())

        self.retranslateUi(BioPIndia)
        self.actionExit.triggered.connect(BioPIndia.close)
        QtCore.QMetaObject.connectSlotsByName(BioPIndia)

    def retranslateUi(self, BioPIndia):
        _translate = QtCore.QCoreApplication.translate
        BioPIndia.setWindowTitle(_translate("BioPIndia", "BioP"))
        self.temperature_sensor_1_label.setText(_translate("BioPIndia", "Temperature Sensor 1"))
        self.temperature_sensor_2_label.setText(_translate("BioPIndia", "Temperature Sensor 2"))
        self.humidity_sensor_1_label.setText(_translate("BioPIndia", "Humidity Sensor 1"))
        self.humidity_sensor_2_label.setText(_translate("BioPIndia", "Humidity Sensor 2"))
        self.Time_label.setText(_translate("BioPIndia", "Time(s)"))
        self.mean_t.setText(_translate("BioPIndia", "Mean"))
        self.temperature.setText(_translate("BioPIndia", "Temperature"))
        self.mean_h.setText(_translate("BioPIndia", "Mean"))
        self.humidity.setText(_translate("BioPIndia", "Humidity"))
        self.smoke.setText(_translate("BioPIndia", "Smoke"))
        self.concentration.setText(_translate("BioPIndia", "Concentration"))
        self.desired_temp_label.setText(_translate("BioPIndia", "Desired Temperature"))
        self.desired_temp_set_pushbox.setText(_translate("BioPIndia", "Set"))
        self.stepper_speed_label.setText(_translate("BioPIndia", "Stepper Speed"))
        self.power_off_button.setText(_translate("BioPIndia", "Power Off"))
        self.label.setText(_translate("BioPIndia", " °C"))
        self.label_2.setText(_translate("BioPIndia", " °C"))
        self.label_3.setText(_translate("BioPIndia", " °C"))
        self.label_4.setText(_translate("BioPIndia", "RH"))
        self.label_5.setText(_translate("BioPIndia", "RH"))
        self.label_6.setText(_translate("BioPIndia", "RH"))
        self.label_7.setText(_translate("BioPIndia", " °C"))
        self.label_8.setText(_translate("BioPIndia", "ppm"))
        self.menuFile.setTitle(_translate("BioPIndia", "File"))
        self.menuEdit.setTitle(_translate("BioPIndia", "Edit"))
        self.menuPort.setTitle(_translate("BioPIndia", "Serial Port"))
        self.menuWebcam_Port.setTitle(_translate("BioPIndia", "Video Device"))
        self.actionView_Loaded_STL_File.setText(_translate("BioPIndia", "View Loaded STL File"))
        self.actionGenerate_GCode_for_STL_File.setText(_translate("BioPIndia", "Generate GCode for STL File"))
        self.actionPrint_via_RepetierHost.setText(_translate("BioPIndia", "Print via RepetierHost"))
        self.actionExit.setText(_translate("BioPIndia", "Exit"))
        self.actionPost_process_GCode_for_BioP.setText(_translate("BioPIndia", "Post process GCode for BioP"))
        self.actionCOM.setText(_translate("BioPIndia", "COM1"))
        self.actionCOM2.setText(_translate("BioPIndia", "COM2"))
        self.actionCOM3.setText(_translate("BioPIndia", "COM3"))
        self.actionLoad_STL_File.setText(_translate("BioPIndia", "Load STL File"))
        self.action1.setText(_translate("BioPIndia", "USB 1"))
        self.action2.setText(_translate("BioPIndia", "USB 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BioPIndia = QtWidgets.QMainWindow()
    ui = Ui_BioPIndia()
    ui.setupUi(BioPIndia)
    BioPIndia.show()
    sys.exit(app.exec_())
