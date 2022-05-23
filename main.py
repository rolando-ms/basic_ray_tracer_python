

def main():
      img_width = 256
      img_height = 256
      with open('image.ppm', 'w') as img:
          img.write('P3\n')
          img.write(str(img_width) + ' ' + str(img_height) + '\n255\n')
          for j in range(img_height-1, 0, -1):
              for i in range(0, img_width):
                  r = i / (img_width - 1)
                  g = j / (img_height - 1)
                  b = 0.25

                  ir = int(255.999 * r)
                  ig = int(255.999 * g)
                  ib = int(255.999 * b)

                  img.write(str(ir) + ' ' + str(ig) + ' ' + str(ib) + '\n')

if __name__ == '__main__':
    main()


