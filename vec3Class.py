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

    def __mul__(self, scalar: float) -> Vec3:
        return Vec3(scalar * self.e)

    def __rmul__(self, scalar: float) -> Vec3:
        return Vec3(self.e * scalar)

    def __truediv__(self, scalar: float) -> Vec3:
        return Vec3(self.e / scalar)

    def length(self) -> float:
        return np.sqrt(self.length_squared())

    def length_squared(self) -> np.ndarray:
        return np.sum(self.e * self.e)

    def unit_vector(self) -> Vec3:
        return Vec3(self.e / np.sqrt(np.sum(self.e * self.e)))


def vec3_dot(v1: Vec3, v2: Vec3) -> np.ndarray:
    return np.dot(v1.e, v2.e)


def vec3_cross(v1: Vec3, v2: Vec3) -> Vec3:
    return Vec3(np.cross(v1.e, v2.e))
