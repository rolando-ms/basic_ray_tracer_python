
from CommonUtilities import *


class Camera:
    def __init__(self, look_from: point3, look_at: point3, vup: Vec3, vfov: float,
                 aspect_ratio: float, aperture: float, focus_dist: float):
        self.aspect_ratio = aspect_ratio
        theta = np.deg2rad(vfov)
        h = np.tan(theta/2)
        self.viewport_height = 2.0 * h
        self. viewport_width = self.aspect_ratio * self.viewport_height

        self.w = (look_from - look_at).unit_vector()
        self.u = vec3_cross(vup, self.w).unit_vector()
        self.v = vec3_cross(self.w, self.u)

        self.origin = look_from
        self.horizontal = focus_dist * self.viewport_width * self.u
        self.vertical = focus_dist * self.viewport_height * self.v
        self.lower_left_corner = self.origin - self.horizontal / 2 - self.vertical / 2 - focus_dist*self.w
        self.lens_radius = aperture / 2

    def get_ray(self, s: float, t: float) -> Ray:
        rd = self.lens_radius * random_in_unit_disk()
        offset = rd.get_x() * self.u + rd.get_y() * self.v
        return Ray(self.origin + offset,
                   self.lower_left_corner + s*self.horizontal + t*self.vertical - self.origin - offset)
