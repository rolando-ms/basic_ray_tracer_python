import numpy as np

from CommonUtilities import *
from colorClass import write_color
from sphereClass import Sphere
from CameraClass import Camera
from MaterialClass import Lambertian
from MaterialClass import Metal
from MaterialClass import Dielectric


def ray_color(r: Ray, world: Hittable, depth: int) -> color:
    rec = HitRecord()

    if depth <= 0:
        return color()

    world_hit, rec = world.hit(r, 0.001, np.Infinity, rec)
    if world_hit:
        scattered = Ray()
        attenuation = color()
        ray_scattered, attenuation, scattered = rec.hit_material.scatter(r, rec, attenuation, scattered)
        if ray_scattered:
            return attenuation * ray_color(scattered, world, depth-1)
        return color()

    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0-t) * color(np.array([1.0, 1.0, 1.0])) + t*color(np.array([0.5, 0.7, 1.0]))


def main():
    # Image
    aspect_ratio = 16.0/9
    img_width = 200
    img_height = int(img_width / aspect_ratio)
    samples_per_pixel = 5
    max_depth = 10

    # World
    world = HittableList()
    # R = np.cos(np.pi/4)
    #
    # material_left = Lambertian(color(np.array([0.0, 0.0, 1.0])))
    # material_right = Lambertian(color(np.array([1.0, 0.0, 0.0])))
    # world.add(Sphere(point3(np.array([-R, 0.0, -1.0])), R, material_left))
    # world.add(Sphere(point3(np.array([R, 0.0, -1.0])), R, material_right))

    material_ground = Lambertian(color(np.array([0.8, 0.8, 0.0])))
    material_center = Lambertian(color(np.array([0.1, 0.2, 0.5])))
    material_left = Dielectric(1.5)
    material_right = Metal(color(np.array([0.8, 0.6, 0.2])), 0.0)

    world.add(Sphere(point3(np.array([0.0, -100.5, -1.0])), 100.0, material_ground))
    world.add(Sphere(point3(np.array([0.0, 0.0, -1.0])), 0.5, material_center))
    world.add(Sphere(point3(np.array([-1.0, 0.0, -1.0])), 0.5, material_left))
    world.add(Sphere(point3(np.array([-1.0, 0.0, -1.0])), -0.45, material_left))
    world.add(Sphere(point3(np.array([1.0, 0.0, -1.0])), 0.5, material_right))

    # Camera
    look_from = point3(np.array([-2, 2, 1]))
    look_at = point3(np.array([0, 0, -1]))
    vup = Vec3(np.array([0, 1, 0]))
    dist_to_focus = (look_from - look_at).length()
    aperture = 2.0
    cam = Camera(look_from, look_at, vup, 30.0, aspect_ratio, aperture, dist_to_focus)

    with open('image.ppm', 'w') as img:
        img.write('P3\n')
        img.write(str(img_width) + ' ' + str(img_height) + '\n255\n')
        for j in range(img_height-1, 0, -1):
            print('\rRows remaining: ' + str(j))
            for i in range(0, img_width):
                pixel_color = color()
                for s in range(samples_per_pixel):
                    u = (i + np.random.rand()) / (img_width - 1)
                    v = (j + np.random.rand()) / (img_height - 1)
                    r = cam.get_ray(u, v)
                    pixel_color += ray_color(r, world, max_depth)
                img.write(write_color(pixel_color, samples_per_pixel))


if __name__ == '__main__':
    main()


