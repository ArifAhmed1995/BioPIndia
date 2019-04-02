from PyQt5.QtGui import QIcon

from text_editor import TextEditor

class GCodeTextBox():
    def __init__(self, gcode_file):
        self.win = TextEditor()
        self.win.setWindowIcon(QIcon.fromTheme("application-text"))
        self.win.setWindowTitle("Plain Text Edit" + "[*]")
        self.win.setMinimumSize(400,600)
        self.win.showMaximized()

        self.gcode_file = gcode_file

    def show(self):
        self.win.openFileOnStart(self.gcode_file)
        self.win.show()
