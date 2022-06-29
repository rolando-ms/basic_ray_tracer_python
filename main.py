import numpy as np

from colorClass import write_color
from CommonUtilities import *
from sphereClass import Sphere
from CameraClass import Camera


def ray_color(r: Ray, world: Hittable) -> color:
    rec = HitRecord()
    world_hit, rec = world.hit(r, 0, np.Infinity, rec)
    if world_hit:
        return 0.5*(rec.normal + color(np.array([1, 1, 1])))
    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0-t) * color(np.array([1.0, 1.0, 1.0])) + t*color(np.array([0.5, 0.7, 1.0]))


def main():
    # Image
    aspect_ratio = 16.0/9
    img_width = 200
    img_height = int(img_width / aspect_ratio)
    samples_per_pixel = 10

    # World
    world = HittableList()
    world.add(Sphere(point3(np.array([0, 0, -1])), 0.5))
    world.add(Sphere(point3(np.array([0, -100.5, -1])), 100))

    # Camera
    cam = Camera()

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
                    pixel_color += ray_color(r, world)
                img.write(write_color(pixel_color, samples_per_pixel))


if __name__ == '__main__':
    main()


