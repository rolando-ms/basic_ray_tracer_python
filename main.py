from colorClass import write_color
from rayClass import Ray
from vec3Class import vec3_dot
from vec3Class import Vec3
import numpy as np

color = Vec3
point3 = Vec3


def hit_sphere(center: point3, radius: float, r: Ray):
    oc = r.origin - center
    a = vec3_dot(r.direction, r.direction)
    b = 2.0 * vec3_dot(oc, r.direction)
    c = -1*(radius * radius) + vec3_dot(oc, oc)
    discriminant = b*b - 4.0*a*c
    if discriminant < 0:
        return -1.0
    else:
        return (-b - np.sqrt(discriminant)) / (2.0*a)


def ray_color(r: Ray) -> color:
    t = hit_sphere(point3(np.array([0.0, 0.0, -1.0])), 0.5, r)
    if t > 0.0:
        N = (r.at(t) - Vec3(np.array([0,0,-1]))).unit_vector()
        return 0.5 * color(np.array([N.x+1, N.y+1, N.z+1]))
    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0-t) * color(np.array([1.0, 1.0, 1.0])) + t*color(np.array([0.5, 0.7, 1.0]))


def main():
    # Image
    aspect_ratio = 16.0/9
    img_width = 400
    img_height = int(img_width / aspect_ratio)

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = point3(np.zeros(3))
    horizontal = Vec3(np.array([viewport_width, 0, 0]))
    vertical = Vec3(np.array([0, viewport_height, 0]))
    lower_left_corner = origin - horizontal/2 - vertical/2 - Vec3(np.array([0, 0, focal_length]))

    with open('image.ppm', 'w') as img:
        img.write('P3\n')
        img.write(str(img_width) + ' ' + str(img_height) + '\n255\n')
        for j in range(img_height-1, 0, -1):
            print('\rRows remaining: ' + str(j))
            for i in range(0, img_width):
                u = i / (img_width - 1)
                v = j / (img_height - 1)
                r = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
                pixel_color = ray_color(r)
                img.write(write_color(pixel_color))


if __name__ == '__main__':
    main()


