#! /usr/bin/python

import argparse
from   src.maestro       import Maestro
from   src.norberg       import Norberg
from   src.joint_control import JointControl


p = argparse.ArgumentParser()

p.add_argument('-j', '--joints',    action='store_true', help='Control joint angles')
p.add_argument('-c', '--cartesian', action='store_true', help='Control Cartesian coordinates')
p.add_argument('type', help='Maestro or Norberg')

args = p.parse_args()

if args.type == 'Maestro':
    if args.joints:
        JointControl(Maestro()).go()
    if args.cartesian:
        pass

if args.type == 'Norberg':
    if args.joints:
        JointControl(Norberg()).go()
    if args.cartesian:
        pass

p.print_help()
