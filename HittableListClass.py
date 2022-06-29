
from CommonUtilities import *


class HittableList(Hittable):
    def __init__(self):
        self.hit_list = []

    def add(self, hit_object):
        self.hit_list.append(hit_object)

    def clear(self):
        self.hit_list.clear()

    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> list[bool, HitRecord]:
        hit_anything = False
        closest_so_far = t_max

        for hit_object in self.hit_list:
            hit_object, rec = hit_object.hit(r, t_min, closest_so_far, rec)
            if hit_object:
                hit_anything = True
                closest_so_far = rec.t

        return [hit_anything, rec]
