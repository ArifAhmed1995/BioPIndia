import os
import re
import threading as thr
import serial as srl
import time

import numpy as np

from pyforms 			import BaseWidget
from pyforms.controls 	import ControlBoundingSlider
from pyforms.controls 	import ControlText
from pyforms.controls 	import ControlButton
from pyforms.controls 	import ControlCheckBox
from pyforms.controls 	import ControlCheckBoxList
from pyforms.controls 	import ControlCombo
from pyforms.controls 	import ControlDir
from pyforms.controls 	import ControlDockWidget
from pyforms.controls 	import ControlEmptyWidget
from pyforms.controls 	import ControlFile
from pyforms.controls 	import ControlFilesTree
from pyforms.controls 	import ControlImage
from pyforms.controls 	import ControlList
from pyforms.controls 	import ControlPlayer
from pyforms.controls 	import ControlProgress
from pyforms.controls 	import ControlSlider
from pyforms.controls 	import ControlVisVis
from pyforms.controls 	import ControlVisVisVolume
from pyforms.controls 	import ControlEventTimeline
from pyforms.controls 	import ControlCodeEditor

import pyforms

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

import matplotlib.pyplot as plt
