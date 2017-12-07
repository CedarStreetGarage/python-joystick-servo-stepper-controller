#! /usr/bin/python

from src.joystick import Joystick
from src.loop     import Loop
from src.maestro  import Maestro
from src.norberg  import Norberg


class Main(object):

    multiplier = 0.02

    joint_map = {
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
        self.l = Loop(5)

    def diff(self, a, b):
        return self.j.button(a) - self.j.button(b)

    def loop(self):
        self.c.inc(joint_map['waist'],     self.multiplier * self.j.axis('lx'))
        self.c.inc(joint_map['shoulder'],  self.multiplier * self.j.axis('ly'))
        self.c.inc(joint_map['elbow'],     self.multiplier * self.j.axis('rx'))
        self.c.inc(joint_map['wrist_rot'], self.multiplier * self.j.axis('ry'))
        self.c.inc(joint_map['wrist_x'],   self.multiplier * self.diff('a','b'))
        self.c.inc(joint_map['wrist_y'],   self.multiplier * self.diff('x','y'))

    def print_loop(self):
        for i in self.j.axes():
            print(i + ' - ' + str(self.j.axis(i)))
        for i in self.j.buttons():
            print(i + ' - ' + str(self.j.button(i)))
        print('')

    def go(self):
        self.l.fun(self.loop).start()


Main(Maestro()).go()

