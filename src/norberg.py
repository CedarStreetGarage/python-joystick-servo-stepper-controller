from controller import Controller


class Norberg(Controller):

    def __init__(self):
        Controller.__init__(self, '/dev/???')

    # Manual page 58
    def _send(self, ch, x):
        val = int(100.0 * x)
        cmd = '{}m\n300$P\n1000$R\n{}$G'.format(ch, val)
        self._write(cmd)

