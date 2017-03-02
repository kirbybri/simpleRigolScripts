import os

class UsbTmcDriver:
    def __init__(self, device):
        self.device = device
        self.FILE = os.open(device, os.O_RDWR)

    def write(self, command):
        try:
            os.write(self.FILE, str(command) );
        except:
            print("Error in USB TMC write")

    def read(self, length = 4000):
        data = None
        try:
            data = os.read(self.FILE, length)
        except:
            print("Error in USB TMC read")
        return data

    def getName(self):
        self.write("*IDN?")
        return self.read(300)

    def sendReset(self):
        self.write("*RST")

def getDeviceList():
    dirList=os.listdir("/dev")
    result=list()

    for fname in dirList:
        if(fname.startswith("usbtmc")):
            result.append("/dev/" + fname)

    return result
