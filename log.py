#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import time
import csv

baudrate = 9600
port = "/dev/tty.usbmodem1411"

if len(sys.argv) == 3:
    ser = serial.Serial(sys.argv[1], sys.argv[2])
else:
    print "# Please specify a port and a baudrate"
    print "# using hard coded defaults " + port + " " + str(baudrate)
    ser = serial.Serial(port, baudrate)


while 1:
    stringData = ser.readline()
    dataList = stringData.rstrip().split(' ')
    if (len(dataList) == 3):
    	print dataList[0]
    	with open("bldc_data.csv", "a") as csvfile:
    		csvfile.write('{}, {}, {}\n'.format(dataList[0], dataList[1], dataList[2]))
    time.sleep(1.0)
