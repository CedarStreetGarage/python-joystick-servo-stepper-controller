class Virtual(object):

    def __init__(self):
        self.vals = [0.0] * 6

    def pos(self, ch, x):
        self.vals[ch] = x

    def inc(self, ch, x):
        self.pos(ch, self.vals[ch] + x)

