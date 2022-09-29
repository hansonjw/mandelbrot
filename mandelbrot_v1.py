# This will be code for plotting a Mandlebrot set...

# Useful links:
# https://realpython.com/mandelbrot-set-python/
# https://www.youtube.com/watch?v=FFftmWSzgmk
# https://en.wikipedia.org/wiki/Benoit_Mandelbrot

# Formally, the Mandelbrot set is the set of complex numbers, c, for which an infinite sequence of numbers, z0, z1, …, zn, …, remains bounded.

import matplotlib.pyplot as plt
from PIL import Image

import numpy as np

colStr = "magma"
# colStr = "binary"
num_iterations = 20
pixel_density=512


# c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
xLow = -2
xHi = 0.5
yLow = -1.5
yHi = 1.5

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax-ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

c = complex_matrix(xLow, xHi, yLow, yHi, pixel_density)


# Matplot - visualization library
# plt.imshow(is_stable(c, num_iterations), cmap=colStr)
# plt.gca().set_aspect("equal")
# plt.axis("off")
# plt.tight_layout()
# plt.show()


# Pillow - PIL, python imaging library
image = Image.fromarray(~is_stable(c, num_iterations=20))
image.show()