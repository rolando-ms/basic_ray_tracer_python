from __future__ import annotations
import numpy as np


class Vec3:
    def __init__(self, vector: np.array = np.zeros(3)):
        self.e = vector
        self.x = self.e[0]
        self.y = self.e[1]
        self.z = self.e[2]

    def __str__(self):
        return 'e[0] = {0}, e[1] = {1}, e[2] = {2}'.format(self.e[0], self.e[1], self.e[2])

    def __add__(self, other: Vec3) -> Vec3:
        # return Vec3(np.array([self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2]]))
        return Vec3(self.e + other.e)

    def __sub__(self, other: Vec3) -> Vec3:
        # return Vec3(np.array([self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2]]))
        return Vec3(self.e - other.e)

    def __rsub__(self, scalar: float) -> Vec3:
        return Vec3(self.e - scalar)

    def __rmul__(self, scalar: float) -> Vec3:
        return Vec3(scalar * self.e)

    def __mul__(self, other: Vec3) -> Vec3:
        return Vec3(self.e * other.e)

    def __truediv__(self, scalar: float) -> Vec3:
        return Vec3(self.e / scalar)

    def get_x(self) -> np.ndarray:
        return self.e[0]

    def get_y(self) -> np.ndarray:
        return self.e[1]

    def get_z(self) -> np.ndarray:
        return self.e[2]

    def length(self) -> float:
        return np.sqrt(self.length_squared())

    def length_squared(self) -> np.ndarray:
        return np.sum(self.e * self.e)

    def unit_vector(self) -> Vec3:
        return Vec3(self.e / np.sqrt(np.sum(self.e * self.e)))

    def near_zero(self):
        s = 1e-8
        return np.abs(self.e[0]) < s and np.abs(self.e[1]) < s and np.abs(self.e[2]) < s


def vec3_dot(v1: Vec3, v2: Vec3) -> np.ndarray:
    return np.dot(v1.e, v2.e)


def vec3_cross(v1: Vec3, v2: Vec3) -> Vec3:
    return Vec3(np.cross(v1.e, v2.e))


def get_random_vec() -> Vec3:
    return Vec3(np.array([np.random.rand(), np.random.rand(), np.random.rand()]))


def get_random_vec_in_range(min: float, max: float) -> Vec3:
    return Vec3(np.array([np.random.uniform(min, max), np.random.uniform(min, max), np.random.uniform(min, max)]))


def random_in_unit_sphere() -> Vec3:
    while True:
        p = get_random_vec_in_range(-1, 1)
        if p.length_squared() >= 1:
            continue
        return p


def random_in_unit_disk():
    while True:
        p = Vec3(np.array([np.random.uniform(-1, 1), np.random.uniform(-1, 1), 0.0]))
        if p.length_squared() >= 1.0:
            continue
        return p


def random_unit_vector() -> Vec3:
    return random_in_unit_sphere().unit_vector()


def vec3_reflect(v: Vec3, n: Vec3) -> Vec3:
    return v - 2*vec3_dot(v, n)*n


def vec3_refract(uv: Vec3, n: Vec3, etai_over_etat: float) -> Vec3:
    cos_theta = np.minimum(vec3_dot(-1*uv, n), 1.0)
    r_out_perp = etai_over_etat * (uv + cos_theta*n)
    r_out_parallel = (-1*np.sqrt(np.abs(1.0 - r_out_perp.length_squared()))) * n
    return r_out_perp + r_out_parallel
