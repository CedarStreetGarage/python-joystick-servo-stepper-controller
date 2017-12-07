import sys   
import serial


TTY = '/dev/ttyACM0'
DEV = 0x0c


class Maestro(object):

    def __init__(self):
        self.serial = serial.Serial(TTY)
        self.prefix = chr(0xaa) + chr(DEV)
        self.vals   = [0.0] * 6

    def _send(self, op, ch, x):
        val = int(6000.0 * x + 3000.0)
        lsb = val & 0x7f 
        msb = (val >> 7) & 0x7f 
        cmd = self.prefix + chr(op) + chr(ch) + chr(lsb) + chr(msb)
        if sys.version_info[0] == 2:
            self.serial.write(cmd)
        else:
            self.serial.write(bytes(cmd, 'latin-1'))

    def pos(self, ch, x):
        self.vals[ch] = x
        self._send(0x04, ch, self.vals[ch])

    def inc(self, ch, x):
        self.pos(self.vals[ch] + x)

