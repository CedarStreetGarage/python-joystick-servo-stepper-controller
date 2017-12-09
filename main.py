#! /usr/bin/python

from src.joystick import Joystick
from src.loop     import Loop
from src.quantize import Quantize
from src.maestro  import Maestro
from src.norberg  import Norberg


class Main(object):

    rate = 20
    mult = 0.02
    prec = 0.02
    jmap = {
        'waist':     0,
        'shoulder':  1,
        'elbow':     2,
        'wrist_rot': 3,
        'wrist_x':   4,
        'wrist_y':   5
    }

    def __init__(self, controller):
        self.c = controller
        self.j = Joystick()
        self.l = Loop(self.rate)
        self.q = Quantize(self.prec)

    def _set_joints(self):
        lx = self.q.quantize(self.j.axis('lx'))
        ly = self.q.quantize(self.j.axis('ly'))
        rx = self.q.quantize(self.j.axis('rx'))
        ry = self.q.quantize(self.j.axis('ry'))
        wx = self.q.quantize(self.j.button('b') - self.j.button('a'))
        wy = self.q.quantize(self.j.button('y') - self.j.button('x'))
        self.c.inc(self.jmap['waist'],     self.mult * lx)
        self.c.inc(self.jmap['shoulder'],  self.mult * ly)
        self.c.inc(self.jmap['elbow'],     self.mult * rx)
        self.c.inc(self.jmap['wrist_rot'], self.mult * ry)
        self.c.inc(self.jmap['wrist_x'],   self.mult * wx)
        self.c.inc(self.jmap['wrist_y'],   self.mult * wy)

    def _print_joystick(self):
        for i in self.j.axes():
            print('{} - {}'.format(i, self.j.axis(i)))
        for i in self.j.buttons():
            print('{} - {}'.format(i, self.j.button(i)))
        print('')

    def _print_controller(self):
        for i, x in enumerate(self.c.vals):
            print('{} - {}'.format(i, x))
        print('')

    def loop(self):
        self._set_joints()
        self._print_joystick()
        self._print_controller()

    def go(self):
        self.l.fun(self.loop).start()


Main(Maestro()).go()

