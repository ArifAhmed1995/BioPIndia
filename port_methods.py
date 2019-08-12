from serial.tools import list_ports

def find_arduino(existing_devices):
    while True:
        arduino_found = False
        serial_devices = list(list_ports.comports())

        for device in serial_devices:
            if device.manufacturer is not None and "Arduino" in device.manufacturer and device not in existing_devices:
                arduino_found = True
                keyfile = open("activation_key.txt", "a+")
                serial = device.serial_number
                keyfile.write(serial+"\n")
                keyfile.close()
                existing_devices.append(device)
                return device.device # Returns Arduino device.
        if not arduino_found:
            print("The arduino was not connected to the host device")
            input("Press enter once you have connected it.......")
            continue

class PortMethods:
    def __init__(self):
        keyfile = open("activation_key.txt", "r")

        self.sensors_key = keyfile.readline()[:-1]
        self.extruder_key = keyfile.readline()[:-1]

        self.sensors_device = None
        self.extruder_device = None

        self.devices = []

        keyfile.close()

        if self.sensors_key == "" or self.extruder_key == "":
            print("Activation key not found !")
            print("Let's set up the printer.")
            print("Please disconnect all Arduinos from the computer. Disconnecting other serial devices is not necessary.")
            print("Connect the sensors arduino please.....")
            input("Once that's done, Press enter to continue.....")

            self.sensors_device = find_arduino(self.devices) # This sets the sensors device.

            print("Sensors found ! Connect the extruder arduino please.....")
            input("Once that's done, Press enter to continue.....")

            self.extruder_device = find_arduino(self.devices) # This sets the extruder device.
        else:
            serial_devices = list(list_ports.comports())

            for serial_device in serial_devices:
                if serial_device.serial_number == self.sensors_key:
                    self.sensors_device = serial_device.device
                elif serial_device.serial_number == self.extruder_key:
                    self.extruder_device = serial_device.device

    def get_sensors_port(self):
        return self.sensors_device

    def get_extruder_port(self):
        return self.extruder_device
