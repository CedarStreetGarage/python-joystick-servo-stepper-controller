from controller import Controller


class Maestro(Controller):

    def __init__(self):
        Controller.__init__(self, '/dev/ttyACM0')
        self.prefix = chr(0xaa) + chr(0x0c) + chr(0x04)

    def _send(self, ch, x):
        val = int(6000.0 * x + 3000.0)
        lsb = val & 0x7f 
        msb = (val >> 7) & 0x7f 
        cmd = self.prefix + chr(ch) + chr(lsb) + chr(msb)
        self._write(cmd)

