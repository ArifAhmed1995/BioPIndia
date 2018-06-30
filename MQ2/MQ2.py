import re
import serial

class MQ2:
    def __init__(self, port="/dev/ttyUSB0", baudrate = 9600):
        self.port = port
        self.baudrate = baudrate
        self.threshold = 400

        #TODO : Check if these params actually work in reality
        self.mq2 = serial.Serial(self.port, baudrate=self.baudrate,
                                 bytesize=serial.EIGHTBITS,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 timeout=2, xonxoff=0, rtscts=0)

        #TODO : Check if 2 seconds is enough for arduino to reset
        time.sleep(2)

        self.active = self.mq2.isOpen()

    def is_active(self):
        return self.active

    def flush(self):
        # Flush the port
        self.mq2.readline()

    def get_and_print_status(self):
        with self.mq2:
            sensor_data = re.match(r"A0:([-]{0,1}\d+)",
                                str(self.mq2.readline()))
            if(sensor_data != None):
                if sensor_data > self.threshold:
                    print("GREEN")
                else:
                    print("RED")

def main():
    sensor = MQ2(port="/dev/ttyUSB0", baudrate = 9600)
    sensor.flush()
    if sensor.is_active():
        sensor.get_and_print_status()

main()
