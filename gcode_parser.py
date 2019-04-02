import serial

class GCodeParser():
    def __init__(self):
        # GCode is parsed into list of serial commands which are then executed by the Arduino
        self.serial_commands = []

        # Non-existent commands:
        # The following commands will not be ignored by the parser
        # The reason is mentioned beside
        # G21 - BioP printing will all happen in mm
        # G90 - Absolute coordinates will always be used
        # M82 - Absolute distances will always be used
        #
        #
        #
        self.slic3r_to_arduino_dictionary = {
            "M107" : "digitalWrite(FAN_PIN, LOW);"
            "G28" :
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
        command_class = len(command)

        if command_class == 1:
            # M107
            pass
        elif len(command) == 2:
            pass

    def parseGCode(self, gcode):
        # serial_commands are filled up here
        gcode = gcode.split("\n")
        for line in gcode:
            line_spl = self.separateCommandComment(line)
            command, comment = line_spl
            self.commandHandler(command)
            # Comments in Slic3r generated GCode are quite important
            # and required to set various physical parameters of the BioP
            # but for now let's focus on the extruder commands.
            #if len(command) < 1:
            #    self.serial_commands.append(self.slic3r_to_arduino_dictionary[command])

    def executeSerialScript(self):
        # Rest of the Magick happens here...
        # Iterate over serial_commands are send to Arduino
        pass
