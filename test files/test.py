
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Arduino" in p[1]:
        arduino = serial.Serial(p[0],9600, timeout=.1)
        while True:
            data = arduino.readline()[:-2] #remove /r/n
            if data:
                print (data)
