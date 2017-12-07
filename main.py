#! /usr/bin/python

from src.joystick import Joystick
from src.loop     import Loop
from src.maestro  import Maestro
from src.norberg  import Norberg


LOOP_TIME     = 0.25
BUTTON_STEP   = 0.02
JOYSTICK_MULT = 0.2


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
        waist     = JOYSTICK_MULT * self.j.axis('lx')
        shoulder  = JOYSTICK_MULT * self.j.axis('ly')
        elbow     = JOYSTICK_MULT * self.j.axis('rx')
        wrist_rot = JOYSTICK_MULT * self.j.axis('ry')
        wrist_x   = BUTTON_STEP * (self.j.button('a') - self.j.button('b'))
        wrist_y   = BUTTON_STEP * (self.j.button('x') - self.j.button('y'))
        self.c.inc(joint_map['waist'],     waist)
        self.c.inc(joint_map['shoulder'],  shoulder)
        self.c.inc(joint_map['elbow'],     elbow)
        self.c.inc(joint_map['wrist_rot'], wrist_rot)
        self.c.inc(joint_map['wrist_x'],   wrist_x)
        self.c.inc(joint_map['wrist_y'],   wrist_y)

    def print_loop(self):
        for i in self.j.axes():
            print(i + ' - ' + str(self.j.axis(i)))
        for i in self.j.buttons():
            print(i + ' - ' + str(self.j.button(i)))
        print('')

    def go(self):
        self.l.fun(self.loop).start()


Main(Maestro()).go()

