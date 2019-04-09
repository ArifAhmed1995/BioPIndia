'''
Command parser for transmitting to extruder set-up controller

Parameters for each function is same so that we don't have to write a ton of conditionals in
gcode_parser

'''
class Commands(object):
    def __init__(self):
        '''
        Reads in the X,Y,Z and other attribute records from the printer_attributes
        '''
        self.attributes = {}
        f = open("printer_attributes.txt", "r")# TODO : Change to an INI/CONF file later
        for line in f:
            entry = (line[:-1]).split("=")
            self.attributes[entry[0]] = int(entry[1])

    def linear_move_in_mm(self, step_angle, timing_pulley_diameter):
        '''Calculate linear move in mm given a step angle and timing pulley diameter

        Least count of any linear movement is 0.125663706(currently for step angle 1.8 and diameter 8 mm)
        '''
        return step_angle * timing_pulley_diameter * 0.00872664625

    def mm_to_iterations(self, linear_distance, step_angle, timing_pulley_diameter):
        mm_per_iteration = self.linear_move_in_mm(step_angle, timing_pulley_diameter)
        iterations = int(linear_distance/ mm_per_iteration)
        return iterations

    def M106(self, arduino, *args):
        '''
        Usually there are many arguments supplied but I think for us
        the fan is simple. It's either ON or OFF.
        '''
        arduino.write(('01').encode('utf-8'))
        #print('01')

    def M107(self, arduino, *args):
        '''
        Usually there are many arguments supplied but I think for us
        the fan is simple. It's either ON or OFF.
        '''
        arduino.write(('02').encode('utf-8'))
        #print('02')

    def G1(self, arduino, *args):
        '''
        Usage
        ------

        G0 Xnnn Ynnn Znnn Ennn Fnnn Snnn
        G1 Xnnn Ynnn Znnn Ennn Fnnn Snnn

        Parameters
        -----------

        Not all parameters need to be used, but at least one has to be used
        Xnnn The position to move to on the X axis
        Ynnn The position to move to on the Y axis
        Znnn The position to move to on the Z axis
        Ennn The amount to extrude between the starting point and ending point
        Fnnn The feedrate per minute of the move between the starting point and ending point (if supplied)
        Hnnn (RepRapFirmware) Flag to check if an endstop was hit (S1 to check, S0 to ignore, S2 see note, default is S0)1
        Snnn Laser cutter/engraver power. In RepRapFirmware, when not in laser mode S in interpreted the same as H.
        '''
        G1_args = args[0]

        x_coord = None
        y_coord = None
        z_coord = None

        step_angle = 1.8
        timing_pulley_diameter = 8

        # Ignore E value for now.
        for arg in G1_args:
            if len(arg) > 1:
                if(arg[0] == 'X'):
                    x_coord = float(arg[1:])
                elif(arg[0] == 'Y'):
                    y_coord = float(arg[1:])
                elif(arg[0] == 'Z'):
                    z_coord = float(arg[1:])

        #TODO : Make this block less repetitive. Easy to do
        if x_coord is not None:
            linear_distance_x = x_coord - self.attributes['X']
            x_stepper_dir = 1 if linear_distance_x > 0 else 0

            linear_distance_x = abs(linear_distance_x)
            x_stepper_iterations = self.mm_to_iterations(linear_distance_x, step_angle, timing_pulley_diameter)

            if x_stepper_dir > 0:
                arduino.write(('05').encode('utf-8'))
                #print('05')
            else:
                arduino.write(('06').encode('utf-8'))
                #print('06')

            x_stepper_iterations = str(x_stepper_iterations)
            arduino.write((x_stepper_iterations).encode('utf-8'))
            #print("X ", x_stepper_iterations)

        if y_coord is not None:
            linear_distance_y = y_coord - self.attributes['Y']
            y_stepper_dir = 1 if linear_distance_y > 0 else 0

            linear_distance_y = abs(linear_distance_y)
            y_stepper_iterations = self.mm_to_iterations(linear_distance_y, step_angle, timing_pulley_diameter)

            if y_stepper_dir > 0:
                arduino.write(('03').encode('utf-8'))
                #print('03')
            else:
                arduino.write(('04').encode('utf-8'))
                #print('04')

            y_stepper_iterations = str(y_stepper_iterations)
            arduino.write((y_stepper_iterations).encode('utf-8'))
            #print("Y ", y_stepper_iterations)

        if z_coord is not None:
            linear_distance_z = z_coord - self.attributes['Z']
            z_stepper_dir = 1 if linear_distance_z > 0 else 0

            linear_distance_z = abs(linear_distance_z)
            z_stepper_iterations = self.mm_to_iterations(linear_distance_z, step_angle, timing_pulley_diameter)

            if z_stepper_dir > 0:
                arduino.write(('07').encode('utf-8'))
                #print('07')
            else:
                arduino.write(('08').encode('utf-8'))
                #print('08')
            z_stepper_iterations = str(z_stepper_iterations)
            arduino.write((z_stepper_iterations).encode('utf-8'))
            #print("Z ", z_stepper_iterations)