
from CommonUtilities import *
color = Vec3


class HitRecord:
    def __init__(self):
        self.p = Vec3()
        self.normal = Vec3()
        self.hit_material = Material()
        self.t = 0.0
        self.front_face = False

    def set_face_normal(self, r: Ray, outward_normal: Vec3):
        self.front_face = vec3_dot(r.direction, outward_normal) < 0
        if self.front_face:
            self.normal = outward_normal
        else:
            self.normal = -1*outward_normal


class Material:
    def scatter(self, r_in: Ray, rec: HitRecord, attenuation: color, scattered: Ray) -> list[bool, float, Ray]:
        pass


class Lambertian(Material):
    def __init__(self, albedo: color = color()):
        self.albedo = albedo

    def scatter(self, r_in: Ray, rec: HitRecord, attenuation: color, scattered: Ray) -> list[bool, float, Ray]:
        scatter_direction = rec.normal + random_unit_vector()

        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered = Ray(rec.p, scatter_direction)
        attenuation = self.albedo
        return [True, attenuation, scattered]


class Metal(Material):
    def __init__(self, albedo: color = color()):
        self.albedo = albedo

    def scatter(self, r_in: Ray, rec: HitRecord, attenuation: color, scattered: Ray) -> list[bool, float, Ray]:
        reflected = vec3_reflect(r_in.direction.unit_vector(), rec.normal)
        scattered = Ray(rec.p, reflected)
        attenuation = self.albedo
        return [vec3_dot(scattered.direction, rec.normal) > 0, attenuation, scattered]
