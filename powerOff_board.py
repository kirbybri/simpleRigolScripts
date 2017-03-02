#!/usr/bin/env python2
import sys
import usbtmc
import time

#define write command
def w(command, din):
    if len(command) < 30: print command
    din.write(command)
    time.sleep(0.2)

def runCommand(nameRequired,chRequired):
    if len(nameRequired) < 5 :
        return
    #find required device
    usbDev = None
    listOfDevices = usbtmc.getDeviceList()
    for dn in listOfDevices:
        d = usbtmc.UsbTmcDriver(dn)
        name = d.getName()
        name = name[:-1]
        #print name
        if name == nameRequired :
            usbDev = dn
            #print "SUCCESS" + str(dn)

        #Exit if required device not found
        if usbDev == None:
            print "Error powerOff : could not find required device. Exiting"
            sys.exit(0) 
	
        #get device interface object
        d = usbtmc.UsbTmcDriver(usbDev)
        #print d.getName()

        if chRequired[0] == 1:
            w(":OUTP CH1,OFF",d)
        if chRequired[1] == 1:
            w(":OUTP CH2,OFF",d)
        if chRequired[2] == 1:
            w(":OUTP CH3,OFF",d)

#define device name and required channels
#nameRequired = "RIGOL TECHNOLOGIES,DP832,DP8C164754059,00.01.11"
#chRequired = [1,0,0]
runCommand("", [1,1,1] )
runCommand("", [1,1,1] )
