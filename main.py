#! /usr/bin/python

import argparse
from   src.control.maestro import Maestro
from   src.control.norberg import Norberg
from   src.joint_control   import JointControl
from   src.ik_control      import InverseKinematicControl


p = argparse.ArgumentParser()

p.add_argument('-j', '--joints',    action='store_true', help='control joint angles')
p.add_argument('-c', '--cartesian', action='store_true', help='control Cartesian coordinates')
p.add_argument('-m', '--maestro',   action='store_true', help='use Maestro servo controller')
p.add_argument('-n', '--norberg',   action='store_true', help='use Norberg SD6DX controller')

args = p.parse_args()

if args.joints and args.maestro:
    JointControl(Maestro()).go()
if args.joints and args.norberg:
    JointControl(Norberg()).go()
if args.cartesian and args.maestro:
    InverseKinematicControl(Maestro()).go()
if args.cartesian and args.norberg:
    InverseKinematicControl(Norberg()).go()

p.print_help()
