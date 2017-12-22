import sys
import serial
from   virtual_controller import VirtualController


class Controller(VirtualController):

    def __init__(self, device):
        VirtualController.__init__(self)
        self.serial = serial.Serial(device)

    def _write(self, cmd):
        if sys.version_info[0] == 2:
            self.serial.write(cmd)
        else:
            self.serial.write(bytes(cmd, 'latin-1'))

