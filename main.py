#! /usr/bin/python

from src.joystick import Joystick
from src.loop     import Loop
from src.maestro  import Maestro
from src.norberg  import Norberg


class Main(object):

    rate = 20
    mult = 0.02
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

    def diff(self, a, b):
        return self.j.button(a) - self.j.button(b)

    def _set_joints(self):
        self.c.inc(self.jmap['waist'],     self.mult * self.j.axis('lx'))
        self.c.inc(self.jmap['shoulder'],  self.mult * self.j.axis('ly'))
        self.c.inc(self.jmap['elbow'],     self.mult * self.j.axis('rx'))
        self.c.inc(self.jmap['wrist_rot'], self.mult * self.j.axis('ry'))
        self.c.inc(self.jmap['wrist_x'],   self.mult * self.diff('a','b'))
        self.c.inc(self.jmap['wrist_y'],   self.mult * self.diff('x','y'))

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

