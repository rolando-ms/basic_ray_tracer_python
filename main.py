from colorClass import write_color
from vec3Class import vec3
import numpy as np

def main():
    img_width = 256
    img_height = 256
    with open('image.ppm', 'w') as img:
        img.write('P3\n')
        img.write(str(img_width) + ' ' + str(img_height) + '\n255\n')
        for j in range(img_height-1, 0, -1):
            print('\rRows remaining: ' + str(j))
            for i in range(0, img_width):
                pixel_color = vec3(np.array([i/(img_width-1), j/(img_height-1), 0.25]))
                img.write(write_color(pixel_color))


if __name__ == '__main__':
    main()


