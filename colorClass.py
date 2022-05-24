from vec3Class import vec3


def write_color(color: vec3) -> str:
    return  str(255.999 * color.x) + ' ' + \
            str(255.999 * color.y) + ' ' + \
            str(255.999 * color.z) + '\n'
