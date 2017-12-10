import numpy as np


class Quantize(object):

    def __init__(self, precision):
        self.steps = 1.0 / precision

    def get(self, x):
        return np.round(x * self.steps) / self.steps

