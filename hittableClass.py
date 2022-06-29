
from CommonUtilities import *


class HitRecord:
    def __init__(self):
        self.p = Vec3()
        self.normal = Vec3()
        self.t = 0.0
        self.front_face = False

    def set_face_normal(self, r: Ray, outward_normal: Vec3):
        self.front_face = vec3_dot(r.direction, outward_normal) < 0
        if self.front_face:
            self.normal = outward_normal
        else:
            self.normal = -1*outward_normal


class Hittable:
    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> list[bool, HitRecord]:
        pass
