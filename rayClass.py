from vec3Class import Vec3

point3 = Vec3


class Ray:
    def __init__(self, origin: point3 = Vec3(), direction: Vec3 = Vec3()):
        self.origin = origin
        self.direction = direction

    def at(self, t: float) -> Vec3:
        return self.origin + t*self.direction
