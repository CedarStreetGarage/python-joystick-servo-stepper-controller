class VirtualController(object):

    def __init__(self):
        self.vals = [0.0] * 6

    def _send(ch, x):
        pass

    def pos(self, ch, x):
        self.vals[ch] = x
        self._send(ch, self.vals[ch])

    def inc(self, ch, x):
        self.pos(ch, self.vals[ch] + x)

