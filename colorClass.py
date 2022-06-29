from CommonUtilities import *


def write_color(colour: Vec3) -> str:
    return  str(255.999 * colour.x) + ' ' + \
            str(255.999 * colour.y) + ' ' + \
            str(255.999 * colour.z) + '\n'
