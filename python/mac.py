#ref:http://www.instructables.com/id/Interface-Arduino-to-MySQL-using-Python/?ALLSTEPS
import mysql.connector
import serial.tools.list_ports

config = {
  'user': 'root',
  'password': 'toor',
  'host': '71.183.68.119:22',
  'database': 'cycle',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)
cursor = link.cursor();
ports = list(serial.tools.list_ports.comports())
for p in ports:
    #if "ttyACM" in p[1]: #fpr raspi
    if "Arduino" in p[1]: #for mac
        #arduino = serial.Serial('/dev'+p[1],9600,timeout = .1) #for raspi
        arduino = serial.Serial(p[0],9600,timeout = .1) #for mac
        while True:
            data = arduino.readline()[:-2]
            if len(data) >0: #prevent empty string
                pieces = data.split(",") #create array
                print(pieces)
                #insert into mysql
                cursor.execute("INSERT INTO `data` (`Date`,`Time`,`Status`,`Position`) VALUES (%s,%s,%s,%s)",(pieces[0],pieces[1],pieces[2],pieces[3]))
                link.commit()
