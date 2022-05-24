from vec3Class import Vec3


def write_color(color: Vec3) -> str:
    return  str(255.999 * color.x) + ' ' + \
            str(255.999 * color.y) + ' ' + \
            str(255.999 * color.z) + '\n'
