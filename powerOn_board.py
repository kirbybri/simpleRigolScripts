import sys
import usbtmc
import time

#define write command
def w(command, din):
    if len(command) < 30: 
        print( str(command) )
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
        if name == None :
            continue
        if len( str(name) ) == 0:
            continue
        name = name[:-1]
        print( name )
        
        if name == nameRequired :
            usbDev = dn
            #print( "SUCCESS" + str(dn) )
            break

    #Exit if required device not found
    if usbDev == None:
        print( "Error powerOff : could not find required device. Exiting" )
        return 
	
    #get device interface object
    d = usbtmc.UsbTmcDriver(usbDev)
    #print d.getName()

    if chRequired[0] == 1:
        w(":OUTP CH1,ON",d)
    if chRequired[1] == 1:
        w(":OUTP CH2,ON",d)
    if chRequired[2] == 1:
        w(":OUTP CH3,ON",d)

#define device name and required channels
#chRequired = [1,0,0]
runCommand("", [1,1,1] )
#runCommand("", [1,1,1] )
