
from CommonUtilities import *


class Sphere(Hittable):
    def __init__(self, center: point3 = point3(), radius: float = 0.0):
        self.center = center
        self.radius = radius

    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> list[bool, HitRecord]:
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = vec3_dot(oc, r.direction)
        c = -1 * (self.radius * self.radius) + oc.length_squared()
        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return [False, rec]
        sqrtd = np.sqrt(discriminant)
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return [False, rec]

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)

        return [True, rec]
