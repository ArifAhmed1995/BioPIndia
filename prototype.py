import os
import subprocess

from __init__ import *

from post_process import *
#from distutils.core import setup
#from Cython.Distutils import build_ext

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def display_stl_external(stl_path):
    fstl = CURRENT_DIR + "/fstl/build/fstl " + stl_path
    subprocess.check_call(fstl, stdout=subprocess.PIPE, shell=True)

def generate_gcode(stl_path):
    generate_command = "perl "+ CURRENT_DIR + "/slic3r/slic3r.pl " + stl_path + " --output output.gcode"
    subprocess.check_call(generate_command, stdout=subprocess.PIPE, shell=True)
    return CURRENT_DIR + "/output.gcode"

class BiopIndia(BaseWidget):
    def __init__(self):
        super(BiopIndia, self).__init__('BiopIndia Software')

        self.mainmenu = [
                          {
                            'View': [
                                      {'View Loaded STL File':self.__viewSTLFile}
                                    ],
                            'Generate': [
                                      {'Generate GCode for STL File':self.__generateGCode}
                                    ]
                          }
                        ]
        self._stlfile = ControlFile('Choose a file')

    def __viewSTLFile(self):
        display_stl_external(str(self._stlfile))

    def __generateGCode(self):
        gcode_path = generate_gcode(str(self._stlfile))
        post_process_gcode(gcode_path)

if __name__ == "__main__":
    pyforms.start_app(BiopIndia)
