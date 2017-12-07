import sys
import serial


class Controller(object):

    def __init__(self, device):
        self.serial = serial.Serial(device)
        self.vals   = [0.0] * 6

    def _write(self, cmd):
        if sys.version_info[0] == 2:
            self.serial.write(cmd)
        else:
            self.serial.write(bytes(cmd, 'latin-1'))

    def pos(self, ch, x):
        self.vals[ch] = x
        self._send(ch, self.vals[ch])

    def inc(self, ch, x):
        self.pos(self.vals[ch] + x)

