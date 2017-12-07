# Joystick Servo and Stepper Controls

This is a joystick interface to servos and steppers.  Basically a pluggable
controller for the Pololu Micro Maestro 6-channel servo controller, which
I use for a small servo-actuated 6DOF arm, and the Peter Norberg Consulting 
SD6DX stepper motor controller, which I use with an American Robot MR6200
Merlin 6DOF arm.  In each case the respective controller has to be set up
appropriately, and the specifics of how the joystick engages the control
depends on the controller.



### Controller Documentation

  * [Pololu Micro Maestro](https://www.pololu.com/docs/pdf/0J40/maestro.pdf)

  * [Peter Norberg Consulting SD6DX](https://www.stepperboard.com/PDFDocs/BC6D20NCRouter.pdf)



### Code

Nothing crazy here.  There is a `Joystick` class that is basically a wrapper for 
`pygame` and fairly specific to a Logitch F310 joystick using only some of the 
axes and buttons.  There is a `Loop` class that is allows scheduling a repeated
task on a fixed interval, used for updates.  There are the two controller classes, 
`Maestro` and `Norberg` that accommodate the specifics of the respective controller
while providing a consistent interface (e.g. `pos()` and `inc()` for setting 
either absolute or incremental positions.  For the purposes of joystick control 
only the incremental position is used, though for other types of control the 
direct position control is used.

