import numpy as np

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
    def __init__(self, albedo: color = color(), fuzz: float = 1.0):
        self.albedo = albedo
        self.fuzz = np.clip(fuzz, 0.0, 1.0)

    def scatter(self, r_in: Ray, rec: HitRecord, attenuation: color, scattered: Ray) -> list[bool, color, Ray]:
        reflected = vec3_reflect(r_in.direction.unit_vector(), rec.normal)
        scattered = Ray(rec.p, reflected + self.fuzz*random_in_unit_sphere())
        attenuation = self.albedo
        return [vec3_dot(scattered.direction, rec.normal) > 0, attenuation, scattered]


class Dielectric(Material):
    def __init__(self, index_of_refraction: float):
        self.index_of_refraction = index_of_refraction

    def scatter(self, r_in: Ray, rec: HitRecord, attenuation: color, scattered: Ray) -> list[bool, color, Ray]:
        attenuation = color(np.ones(3))
        refraction_ratio = self.index_of_refraction
        if rec.front_face:
            refraction_ratio = 1.0 / self.index_of_refraction

        unit_direction = r_in.direction.unit_vector()
        refracted = vec3_refract(unit_direction, rec.normal, refraction_ratio)

        scattered = Ray(rec.p, refracted)

        return [True, attenuation, scattered]
