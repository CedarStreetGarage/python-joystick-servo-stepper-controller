# Joystick Servo and Stepper Controls

This is a joystick interface to servos and steppers.  Basically a pluggable
controller for the Pololu Micro Maestro 6-channel servo controller, which
I use for a small servo-actuated 6DOF arm, and the Peter Norberg Consulting 
SD6DX stepper motor controller, which I use with an American Robot MR6200
Merlin 6DOF arm. 



### Controller Documentation

  * [Pololu Micro Maestro](docs/maestro.pdf)

  * [Peter Norberg Consulting SD6DX](docs/norberg.pdf)



### Code

There is a `Joystick` class that is basically a wrapper for `pygame` and is 
fairly specific to a Logitch F310 joystick using only some of the axes and 
buttons.  It is really easy to extend if someone wanted, pretty handy 
set of abstractions.  There is a `Loop` class that is allows scheduling a 
repeated task on a fixed interval, used for updates.  Fixed interval meaning 
fixed time between starting runs, it accommodates the duration of the actual
task, which needs to be less than the desired loop time.  There is a 
`Quantize` class that allows for arbitrary returned precision; this is used
to prevent noise on the joysticks from changing the incremental positions
of the controllers.  There are the two controller classes, `Maestro` and 
`Norberg` that accommodate the specifics of the respective controller. Each 
of these are subclasses of the `Controller` class that provides common 
initialization and a consisten interface for control (e.g. `pos()` and 
`inc()` for setting either absolute or incremental positions).  For the 
purposes of joystick control  only the incremental position is used, though 
for other types of control (e.g. abstracting the joint angles using inverse 
kinematics or similar) the direct position control is used.  There is also
a `Joints` class that is basically just a lookup between English names for
robot joints and the index for the joint used by the controller.

The Maestro controller must be set up in advance using a utility provided
by the manufacturer.  Since this must be done, advantage can be taken of 
configuring the maximum speed, acceleration and stops using the utility 
rather than implementing them in software here. This controller by default 
runs in vector mode with all actions on all servos occuring synchronously.

The Norberg controller is a far more advanced controller intended for 
CNC control.  That said, it has a slew of features not used here (e.g. 
vector control for curve contours, analog-to-digital inputs, etc.).  It
allows either synchronous (vector) or asynchronous control; here we
are using vector control operations.  Despite the controller supporting
relative position control, this is implemented manually.  Reason for that
is it is extremely easy to compute manually and simple to rely only on the
controllers vector implementation of absolute position.



### Future Plans

While this code is an exercise in simple joint controllers that can be
used with a joystick, there are a number of other things the controller
classes are candidates for use with:

  * Actuation for ROS controllers

  * Actuation for inverse kinematics

