
from CommonUtilities import *


def write_color(colour: Vec3, samples_per_pixel: int) -> str:
    r = colour.get_x()
    g = colour.get_y()
    b = colour.get_z()

    scale = 1.0 / samples_per_pixel
    r = np.sqrt(scale * r)
    g = np.sqrt(scale * g)
    b = np.sqrt(scale * b)

    return  str(int(256 * np.clip(r, 0.0, 0.999))) + ' ' + \
            str(int(256 * np.clip(g, 0.0, 0.999))) + ' ' + \
            str(int(256 * np.clip(b, 0.0, 0.999))) + '\n'
