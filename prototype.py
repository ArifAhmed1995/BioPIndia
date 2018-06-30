import os
import subprocess

from __init__ import *

from post_process import *

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def display_stl_external(stl_path):
    fstl = CURRENT_DIR + "/fstl/build/fstl " + stl_path
    subprocess.check_call(fstl, stdout=subprocess.PIPE, shell=True)

def generate_gcode(stl_path):
    generate_command = "slic3r " + stl_path + " --output output.gcode"
    subprocess.check_call(generate_command, stdout=subprocess.PIPE, shell=True)
    return CURRENT_DIR + "/output.gcode"

class BiopIndia(BaseWidget):
    def __init__(self):
        super(BiopIndia, self).__init__('BiopIndia Software')

        self.mainmenu = [
                          {
                            'File': [
                                      {'View Loaded STL File':self.__view_stl_file},
                                      {'Generate GCode for STL File':self.__generate_gcode},
                                      {'Print via Repetier Host':self.__open_rep_host},
                                      {'Exit': self.__exit}
                                    ],
                            'Edit': [
                                      {'Post process GCode for BioP':self.__post_process}
                                    ]
                          }
                        ]
        self._stlfile = ControlFile('Choose a file')

    def __view_stl_file(self):
        display_stl_external(str(self._stlfile))

    def __generate_gcode(self):
        gcode_path = generate_gcode(str(self._stlfile))
        post_process_gcode(gcode_path)

    def __post_process(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        gcodefile, _ = QFileDialog.getOpenFileName(self,"Select a GCode File", "","GCode Files (*.gcode)", options=options)
        post_process_gcode(gcodefile)

    def __open_rep_host(self):
        subprocess.check_call("./Repetier-Host-x86_64-2.1.2.AppImage", stdout=subprocess.PIPE, shell=True)

    def __exit(self):
        exit()

if __name__ == "__main__":
    pyforms.start_app(BiopIndia)
