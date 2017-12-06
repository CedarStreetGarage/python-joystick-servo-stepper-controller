#! /usr/bin/python

from src.joystick import Joystick
from src.loop     import Loop



class Main(object):

    def __init__(self):
        self.j = Joystick()
        self.l = Loop(0.25)

    def printer(self):
        for i in self.j.axes():
            print(i + ' - ' + str(self.j.axis(i)))
        for i in self.j.buttons():
            print(i + ' - ' + str(self.j.button(i)))
        print('')

    def go(self):
        self.l.fun(self.printer).start()
    


Main().go()
