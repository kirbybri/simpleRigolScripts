import usbtmc
import time

listOfDevices = usbtmc.getDeviceList()
print( str( listOfDevices ) )

for dn in listOfDevices:
    d = usbtmc.UsbTmcDriver(dn)
    name = d.getName()
    print( str( name ) )
