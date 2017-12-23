from input.joystick   import Joystick
from other.loop       import Loop
from other.quantize   import Quantize
from constants.joints import Joints


RATE = 20
MULT = 0.02
PREC = 0.02


class JointControl(object):

    def __init__(self, controller):
        self.cont  = controller
        self.joy   = Joystick()
        self.loop  = Loop(RATE)
        self.quant = Quantize(PREC)
        self.joint = Joints()

    def _set_joints(self):
        lx = self.quant.get(self.joy.axis('lx'))
        ly = self.quant.get(self.joy.axis('ly'))
        rx = self.quant.get(self.joy.axis('rx'))
        ry = self.quant.get(self.joy.axis('ry'))
        wx = self.quant.get(self.joy.button('b') - self.joy.button('a'))
        wy = self.quant.get(self.joy.button('y') - self.joy.button('x'))
        self.cont.inc(self.joint.get('waist'),     MULT * lx)
        self.cont.inc(self.joint.get('shoulder'),  MULT * ly)
        self.cont.inc(self.joint.get('elbow'),     MULT * rx)
        self.cont.inc(self.joint.get('wrist_rot'), MULT * ry)
        self.cont.inc(self.joint.get('wrist_x'),   MULT * wx)
        self.cont.inc(self.joint.get('wrist_y'),   MULT * wy)

    def _print_joystick(self):
        for i in self.joy.axes():
            print('{} - {}'.format(i, self.joy.axis(i)))
        for i in self.joy.buttons():
            print('{} - {}'.format(i, self.joy.button(i)))
        print('')

    def _print_controller(self):
        for i, x in enumerate(self.cont.vals):
            print('{} - {}'.format(i, x))
        print('')

    def _loop(self):
        self._set_joints()
        self._print_joystick()
        self._print_controller()

    def go(self):
        self.loop.fun(self._loop).start()

