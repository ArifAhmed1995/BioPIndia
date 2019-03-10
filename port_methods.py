from serial.tools import list_ports

def get_arduino_port():
    keyfile = open("activation_key.txt", "r")
    key_string = keyfile.readline()
    keyfile.close()

    if key_string == "":
        while True:
            serial_devices = list(list_ports.comports())
            if(len(serial_devices) > 1):
                print("More than one serial device connected. Please connect only BioP to your host computer.")
                print("This will enable BioP software to recognise the device. After recognising you can connect other serial devices")
                input("Press enter once you have disconnected other devices.....")
                continue
            else:
                keyfile = open("activation_key.txt", "w")
                serial = serial_devices[0].serial_number
                keyfile.write(serial)
                keyfile.close()
                return serial_devices[0].device # This returns port
    else:
        serial_devices = list(list_ports.comports())
        for serial_device in serial_devices:
            if serial_device.serial_number == key_string:
                return serial_device.device
