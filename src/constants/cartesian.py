class Cartesian(object):

    cartesian_map = {
        'x': 0,
        'y': 1,
        'z': 2
    }

    def get(self, name):
        return self.cartesian_map[name]

