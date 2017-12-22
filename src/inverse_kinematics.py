from joints    import Joints
from cartesian import Cartesian


class InverseKinematics(object):

    def __init__(self):
        self.j = Joints()
        self.c = Cartesian()

    def _decode_cartesian(self, cartesian):
        x = cartesian[self.c['x']]
        y = cartesian[self.c['y']]
        z = cartesian[self.c['z']]
        return x,y,z

    def _compute(self, cartesian):
        return 0,0,0,0,0,0

    def ik(self, cartesian):
        c = self._decode_cartesian(cartesian)
    
