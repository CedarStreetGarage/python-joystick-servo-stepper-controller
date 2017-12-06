#! /usr/bin/python

from src.joystick import Joystick
from src.loop     import Loop
from src.maestro  import Maestro
from src.norberg  import Norberg


LOOP_TIME = 0.25
STEP_SIZE = 0.02


class Main(object):

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
        self.l = Loop(LOOP_TIME)

    def loop(self):
        wx = STEP_SIZE * (self.j.button('a') - self.j.button('b'))
        wy = STEP_SIZE * (self.j.button('x') - self.j.button('y'))
        self.c.set_val(joint_map['waist'],     self.j.axis('lx'))
        self.c.set_val(joint_map['shoulder'],  self.j.axis('ly'))
        self.c.set_val(joint_map['elbow'],     self.j.axis('rx'))
        self.c.set_val(joint_map['wrist_rot'], self.j.axis('ry'))
        self.c.set_inc(joint_map['wrist_x'],   wx)
        self.c.set_inc(joint_map['wrist_y'],   wy)

    def print_loop(self):
        for i in self.j.axes():
            print(i + ' - ' + str(self.j.axis(i)))
        for i in self.j.buttons():
            print(i + ' - ' + str(self.j.button(i)))
        print('')

    def go(self):
        self.l.fun(self.loop).start()


Main(Norberg()).go()

