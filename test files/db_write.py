#!/usr/bin/python
import serial.tools.list_ports
import MySQLdb

db = MySQLdb.connect("localhost","root","toor","cycle") or die ("connection failed")
cursor = db.cursor();

#find arduino
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Arduino" in p[1]:
        arduino = serial.Serial(p[0],9600, timeout=.1)
        while True:
            try:
                data = arduino.readline()[:-2] #remove /r/n
                pieces = data.split(",")
                try:
                    cursor.execute("INSERT INTO cycleData (StartHour,StartMin,StarSec,StartPos,StopHour,StopMin,StopSec,StopPos) VALUES (%s,%s,&s,%s,%s,%s,%s,%s)",(pieces[0],pieces[1],pieces[2],pieces[3],pieces[4],pieces[5],pieces[6],pieces[7]))
                    db.commit();
                    cursor.close();
                except MySQLdb.IntegrityError:
                    print ('failed to insert data')
                finally:
                    cursor.close()
                except:
                    print ('failed to get data from arduino')
