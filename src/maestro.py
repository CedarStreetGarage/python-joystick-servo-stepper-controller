import sys   
import serial


CHANNELS     = 8
SPEED        = 100
ACCELERATION = 100


class Maestro(object):

    def __init__(self, tty='/dev/ttyACM0', device=0x0c):
        self.serial = serial.Serial(tty)
        self.prefix = chr(0xaa) + chr(device)
        self.vals   = [0.0] * CHANNELS 
        self._initialize()

    def _initialize(self):
        self._set_speed()
        self._set_acceleration()
        for i, x in enumerate(self.vals):
            self.set_val(i, x)
        
    def _send(self, cmd):
        if sys.version_info[0] == 2:
            self.serial.write(self.prefix + cmd)
        else:
            self.serial.write(bytes(self.prefix + cmd, 'latin-1'))

    def _byte_map(self, cmd, ch, x):
        lsb = x & 0x7f 
        msb = (x >> 7) & 0x7f 
        return chr(cmd) + chr(ch) + chr(lsb) + chr(msb)

    def _set_speed(self):
        for ch in range(CHANNELS):
            cmd = self._byte_map(0x07, ch, SPEED)
            self._send(cmd)

    def _set_acceleration(self):
        for ch in range(CHANNELS):
            cmd = self._byte_map(0x09, ch, ACCELERATION)
            self._send(cmd)

    def _scale(self, x):
        return int(3000 * (x + 1) + 3000)

    def set_val(self, ch, x):
        self.vals[ch] = x
        cmd = self._byte_map(0x04, ch, self._scale(self.vals[ch]))
        self._send(cmd)

    def set_inc(self, ch, x):
        self.vals[ch] += x
        cmd = self._byte_map(0x04, ch, self._scale(self.vals[ch]))
        self._send(cmd)

