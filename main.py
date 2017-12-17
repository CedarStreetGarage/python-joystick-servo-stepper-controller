#! /usr/bin/python

import argparse
from   src.maestro       import Maestro
from   src.norberg       import Norberg
from   src.joint_control import JointControl


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
    pass
if args.cartesian and args.norberg:
    pass

p.print_help()
