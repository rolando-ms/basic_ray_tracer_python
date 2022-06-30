
from CommonUtilities import *


class Camera:
    def __init__(self, look_from: point3, look_at: point3, vup: Vec3, vfov: float, aspect_ratio: float):
        self.aspect_ratio = aspect_ratio
        theta = np.deg2rad(vfov)
        h = np.tan(theta/2)
        self.viewport_height = 2.0 * h
        self. viewport_width = self.aspect_ratio * self.viewport_height

        w = (look_from - look_at).unit_vector()
        u = vec3_cross(vup, w)
        v = vec3_cross(w, u)

        self.origin = look_from
        self.horizontal = self.viewport_width * u
        self.vertical = self.viewport_height * v
        self.lower_left_corner = self.origin - self.horizontal / 2 - self.vertical / 2 - w

    def get_ray(self, s: float, t: float) -> Ray:
        return Ray(self.origin, self.lower_left_corner + s*self.horizontal + t*self.vertical - self.origin)
