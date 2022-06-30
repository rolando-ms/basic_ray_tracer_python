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


def random_scene() -> HittableList:
    world = HittableList()

    ground_material = Lambertian(color(np.array([0.5, 0.5, 0.5])))
    world.add(Sphere(point3(np.array([0, -1000, 0])), 1000, ground_material))

    for a in range(-11, 11):
        for b in range(-11, 11):
            choose_mat = np.random.rand()
            center = point3(np.array([a + 0.9 * np.random.rand(), 0.2, b + 0.9 * np.random.rand()]))

            if (center - point3(np.array([4, 0.2, 0]))).length() > 0.9:
                if choose_mat < 0.8:
                    # Diffuse
                    albedo = get_random_vec() * get_random_vec()
                    sphere_material = Lambertian(albedo)
                    world.add(Sphere(center, 0.2, sphere_material))
                elif choose_mat < 0.95:
                    # Metal
                    albedo = get_random_vec_in_range(0.5, 1)
                    fuzz = np.random.uniform(0, 0.5)
                    sphere_material = Metal(albedo, fuzz)
                    world.add(Sphere(center, 0.2, sphere_material))
                else:
                    # Glass
                    sphere_material = Dielectric(1.5)
                    world.add(Sphere(center, 0.2, sphere_material))

    material1 = Dielectric(1.5)
    world.add(Sphere(point3(np.array([0, 1, 0])), 1.0, material1))

    material2 = Lambertian(color(np.array([0.4, 0.2, 0.1])))
    world.add(Sphere(point3(np.array([-4, 1, 0])), 1.0, material2))

    material3 = Metal(color(np.array([0.7, 0.6, 0.5])), 0.0)
    world.add(Sphere(point3(np.array([4, 1, 0])), 1.0, material3))

    return world



def main():
    # Image
    aspect_ratio = 3.0/2.0
    img_width = 300
    img_height = int(img_width / aspect_ratio)
    samples_per_pixel = 4
    max_depth = 30

    # World
    world = random_scene()

    # world = HittableList()
    #
    # material_ground = Lambertian(color(np.array([0.8, 0.8, 0.0])))
    # material_center = Lambertian(color(np.array([0.1, 0.2, 0.5])))
    # material_left = Dielectric(1.5)
    # material_right = Metal(color(np.array([0.8, 0.6, 0.2])), 0.0)
    #
    # world.add(Sphere(point3(np.array([0.0, -100.5, -1.0])), 100.0, material_ground))
    # world.add(Sphere(point3(np.array([0.0, 0.0, -1.0])), 0.5, material_center))
    # world.add(Sphere(point3(np.array([-1.0, 0.0, -1.0])), 0.5, material_left))
    # world.add(Sphere(point3(np.array([-1.0, 0.0, -1.0])), -0.45, material_left))
    # world.add(Sphere(point3(np.array([1.0, 0.0, -1.0])), 0.5, material_right))

    # Camera
    look_from = point3(np.array([13, 2, 3]))
    look_at = point3(np.array([0, 0, 0]))
    vup = Vec3(np.array([0, 1, 0]))
    dist_to_focus = 10.0
    aperture = 0.1
    cam = Camera(look_from, look_at, vup, 20.0, aspect_ratio, aperture, dist_to_focus)

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


