from PyQt5.QtGui import QIcon

from text_editor import TextEditor

class GCodeTextBox():
    def __init__(self, gcode_file):
        win = TextEditor()
        win.setWindowIcon(QIcon.fromTheme("application-text"))
        win.setWindowTitle("Plain Text Edit" + "[*]")
        win.setMinimumSize(400,600)
        win.showMaximized()
        win.openFileOnStart(gcode_file)
        win.show()
