class Joints(object):

    joint_map = {
        'waist':     0,
        'shoulder':  1,
        'elbow':     2,
        'wrist_rot': 3,
        'wrist_x':   4,
        'wrist_y':   5
    }

    def get(self, name):
        return self.joint_map[name]
