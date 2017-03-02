#!/usr/bin/env python2

import usbtmc
import time

listOfDevices = usbtmc.getDeviceList()

print listOfDevices

for dn in listOfDevices:
	#dn = listOfDevices[0]
	d = usbtmc.UsbTmcDriver(dn)
	name = d.getName()
	print name
