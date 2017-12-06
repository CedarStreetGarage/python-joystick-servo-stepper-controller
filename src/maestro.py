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

    def _byte_map(self, x):
        lsb = x & 0x7f 
        msb = (x >> 7) & 0x7f 
        return chr(lsb) + chr(msb)

    def _set_speed(self):
        for ch in range(CHANNELS):
            cmd = chr(0x07) + chr(ch) + self._byte_map(SPEED)
            self._send(cmd)

    def _set_acceleration(self):
        for ch in range(CHANNELS):
            cmd = chr(0x09) + chr(ch) + self._byte_map(ACCELERATION)
            self._send(cmd)

    def _scale(self, x):
        return int(3000 * (x + 1) + 3000)

    def set_val(self, ch, x):
        self.vals[ch] = x
        val = self._byte_map(self._scale(self.vals[ch]))
        cmd = chr(0x04) + chr(ch) + val
        self._send(cmd)

    def set_inc(self, ch, x):
        self.vals[ch] += x
        val = self._byte_map(self._scale(self.vals[ch]))
        cmd = chr(0x04) + chr(ch) + val
        self._send(cmd)

