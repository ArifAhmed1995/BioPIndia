import serial
from commands import Commands

class GCodeParser():
    def __init__(self, port):
        # GCode is parsed into list of serial commands which are then executed by the Arduino
        self.serial_commands = []
        self.commands = Commands()
        # Non-existent commands:
        # The following commands will not be ignored by the parser
        # The reason is mentioned beside
        # G21 - BioP printing will all happen in mm
        # G90 - Absolute coordinates will always be used
        # M82 - Absolute distances will always be used
        self.extruder = serial.Serial(port, baudrate=9600,
                                  bytesize=serial.EIGHTBITS,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE,
                                  timeout=2, xonxoff=0, rtscts=0)

        self.slic3r_to_arduino_dictionary = {
                            "M107" : self.commands.M107,
                            "M106" : self.commands.M106,
                            "G1" : self.commands.G1
                        }

    def separateCommandComment(self, line):
        # For some reason, split did not work the expected way
        # hence this function.
        # TODO : Delete this method later
        command = ""
        comment = ""
        for index in range(len(line)):
            if line[index] == ';':
                comment = line[index + 1:]
                break
            else:
                command += line[index]
        return [command, comment]

    def commandHandler(self, command):
        command = command.split(" ")
        command_length = len(command)

        if command_length > 1:
            self.slic3r_to_arduino_dictionary[command[0]](self.extruder, command[1:])
        else:
            self.slic3r_to_arduino_dictionary[command[0]](self.extruder)

    def parseGCode(self, gcode):
        # serial_commands are filled up here
        gcode = gcode.split("\n")
        for line in gcode:
            line_spl = self.separateCommandComment(line)
            command, comment = line_spl
            self.commandHandler(command)
            #Every call of this statement automatically executes that command

            # Comments in Slic3r generated GCode are quite important
            # and required to set various physical parameters of the BioP
            # but for now let's focus on the extruder commands.
            #if len(command) < 1:
            #    self.serial_commands.append(self.slic3r_to_arduino_dictionary[command])

