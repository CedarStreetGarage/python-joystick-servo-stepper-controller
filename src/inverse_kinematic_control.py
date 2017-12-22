from input.joystick             import Joystick
from assist.loop                import Loop
from assist.quantize            import Quantize
from joints                     import Joints
from cartesian                  import Cartesian
from control.virtual_controller import VirtualController
from inverse_kinematics         import InverseKinematics


RATE = 20
MULT = 0.02
PREC = 0.02


class InverseKinematicControl(object):

    def __init__(self, controller):
        self.cont  = controller
        self.joy   = Joystick()
        self.loop  = Loop(RATE)
        self.quant = Quantize(PREC)
        self.joint = Joints()
        self.cart  = Cartesian()
        self.virt  = VirtualController()
        self.ik    = InverseKinematics()

    def _set_waist_shoulder_elbow(self):
        lx = self.quant.get(self.joy.axis('lx'))
        ly = self.quant.get(self.joy.axis('ly'))
        rx = self.quant.get(self.joy.axis('rx'))
        self.virt.pos(self.joint.get('waist'),    MULT * lx)
        self.virt.pos(self.joint.get('shoulder'), MULT * ly)
        self.virt.pos(self.joint.get('elbow'),    MULT * rx)
        # Now the virtual controller has the desired position
        # Need to perform IK and update the physical controller

    def _set_wrist_joints(self):
        ry = self.quant.get(self.joy.axis('ry'))
        wx = self.quant.get(self.joy.button('b') - self.joy.button('a'))
        wy = self.quant.get(self.joy.button('y') - self.joy.button('x'))
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
        self._set_waist_shoulder_elbow()
        self._set_wrist_joints()
        self._print_joystick()
        self._print_controller()

    def go(self):
        self.loop.fun(self._loop).start()

