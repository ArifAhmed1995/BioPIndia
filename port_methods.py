from serial.tools import list_ports

def get_arduino_port():
    keyfile = open("activation_key.txt", "r")
    key_string = keyfile.readline()
    keyfile.close()

    serial_devices = list(list_ports.comports())
    if key_string == "":
        print("Activation key not found ! Make sure no other Arduino based devices")
        print("apart from BioP are connected to host computer. Disconnecting other serial devices is not necessary.")
        input("Press enter to continue.....")
        while True:
            arduino_found = False
            for device in serial_devices:
                if device.manufacturer is not None and "Arduino" in device.manufacturer:
                    arduino_found = True
                    keyfile = open("activation_key.txt", "w")
                    serial = device.serial_number
                    keyfile.write(serial)
                    keyfile.close()
                    return device.device # This returns port
            if not arduino_found:
                print("The BioP was not connected to the host device")
                input("Press enter once you have connected it.......")
                continue
    else:
        for serial_device in serial_devices:
            if serial_device.serial_number == key_string:
                return serial_device.device