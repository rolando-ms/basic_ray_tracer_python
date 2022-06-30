## Basic Ray Tracer

This project contains my python implementation of a basic ray tracer based on the book: [Ray Tracing in one Weekend](https://raytracing.github.io/books/RayTracingInOneWeekend.html)

The code is tested in Windows 10 using Pycharm IDE.


## How to use this repository

* Download this repository.
* Run main file
* Rendered image should be printed in image.ppm
* Open image in a program that supports ppm file extensions (e.g. GIMP).

## Notes

The rendering is done on a single core. I took a couple of hours to render the final image in low quality using the following parameters:
* Img width: 300
* Samples per pixel = 4
* Max depth = 30