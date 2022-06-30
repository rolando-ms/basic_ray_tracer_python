
from rayClass import Ray
from MaterialClass import HitRecord


class Hittable:
    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> list[bool, HitRecord]:
        pass
