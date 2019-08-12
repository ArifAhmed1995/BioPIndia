# BioApp

Software for interfacing with the BioP. Currently in early stages of development.


#### Running the software : `python3 software.py`

#### Required libraries : `pyserial`, `matplotlib`, `numpy`, `PyQt5`, `cv2`

#### Required Tools for Development : `pyuic5`, `Qt5 Designer`

Has been tested on UNIX environment only.

#### Implemented  
 - Temperature and Humidity Live Readings
 - Temperature and Humidity Live Parallel Plots
 - Smoke Concentration Reading
 - Embedded Video Capture
 - GCode Parser(Individual Command Handlers not yet complete)
 - Inbuilt GCode Editor

#### Current Focus   
 - Handlers for various GCode commands(G1 implemented, not tested yet).
 - Correcting CAD tool. Integrated into BioApp, but the tool itself has major issues.
 - Code cleanup. Fit PEP8 standards, better encapsulation where possible.
