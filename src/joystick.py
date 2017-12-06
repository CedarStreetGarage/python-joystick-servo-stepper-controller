import pygame


JOYSTICK = 0


class Joystick(object):

    axis_def   = ['lx','ly','rx','ry']
    button_def = ['x','y','a','b','lb','rb']

    def __init__(self):
        pygame.display.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(JOYSTICK)
        self.joystick.init()
        pygame.event.pump()

    def axes(self):
        return self.axis_def

    def axis(self, axis):
        pygame.event.pump()
        if axis == self.axis_def[0]:
            return self.joystick.get_axis(0)
        if axis == self.axis_def[1]:
            return -self.joystick.get_axis(1)
        if axis == self.axis_def[2]:
            return self.joystick.get_axis(3)
        if axis == self.axis_def[3]:
            return -self.joystick.get_axis(4)

    def buttons(self):
        return self.button_def

    def button(self, button):
        pygame.event.pump()
        if button == self.button_def[0]:
            return self.joystick.get_button(2)
        if button == self.button_def[1]:
            return self.joystick.get_button(3)
        if button == self.button_def[2]:
            return self.joystick.get_button(0)
        if button == self.button_def[3]:
            return self.joystick.get_button(1)
        if button == self.button_def[4]:
            return self.joystick.get_button(4)
        if button == self.button_def[5]:
            return self.joystick.get_button(5)

