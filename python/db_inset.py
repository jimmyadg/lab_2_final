#ref:http://www.instructables.com/id/Interface-Arduino-to-MySQL-using-Python/?ALLSTEPS
import MySQLdb
import serial.tools.list_ports
db = MySQLdb.connect("localhost","root","toor","cycle") or die ("connection failed")
cursor = db.cursor();
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "ttyACM" in p[1]: #fpr raspi
    #if "Arduino" in p[1]: #for mac
        arduino = serial.Serial('/dev'+p[1],9600,timeout = .1) #for raspi
        #arduino = serial.Serial(p[0],9600,timeout = .1) #for mac
        while True:
            data = arduino.readline()[:-2]
            if len(data) >0: #prevent empty string
                pieces = data.split(",") #create array
                print(pieces)
                #insert into mysql
                cursor.execute("INSERT INTO `data` (`Date`,`Time`,`Status`,`Position`) VALUES (%s,%s,%s,%s)",(pieces[0],pieces[1],pieces[2],pieces[3]))
                db.commit()
