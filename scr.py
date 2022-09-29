from mandelbrot import MandelbrotSet
from PIL import Image
from viewport import Viewport
import matplotlib.cm
import numpy as np
from scipy.interpolate import interp1d

# params
scale = 4
max_iterations = 1000
escape_radius = 100
sizeX = 512*scale
sizeY = 512*scale

# Centered on the whole Mandelbrot image
center = -1.778 + 0.007j
width = .002

# Interesting...
# center = -0.625 + .4010j
# width = .001

# Centered on spiral from tutorial
# center=-0.7435 + 0.1314j
# width=0.002

# A cool one!
# center = -.74515 - .12515j
# width = .00005

# near 0, 0
# center = .254981 + .000652j
# width = .00001

def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) -1))
        pixel.color = palette[index % len(palette)]


def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette
    ]



# colors
# exterior = [(.78, .98, .98)] * 50
# interior = [(.1, .1, .2)] * 10
# exterior = [(.1, .1, .2)] * 20
# interior = [(.78, .98, .98)] * 10
# grad2 = [(.1, .1*(1-j/99), .2+.8*(j/99)) for j in range(100)]
# grad1 = [(0, 1-i/199, 1) for i in range(200)]
# palette = denormalize(exterior + grad2 + grad1 + interior)

# new custom methodology
blackBlue = [(b/99, 0, 0) for b in range(100)]
bluePink = [(1-p/99, 0, p/99) for p in range(100)]
pinkCyan = [(c/99, c/99, 1-c/99) for c in range(100)]
cyanGreen = [(g/299, g/299, 1-g/299) for g in range(300)]
greenYellow = [(y/99, 1, 0) for y in range(100)]
yellowRed = [(1, 1-r/99, 0) for r in range(100)]
redGrey = [(.2, .2, .2*(g/499)) for g in range(500)]
palette = denormalize(blackBlue + bluePink + pinkCyan + cyanGreen)

# 
# colormap = matplotlib.cm.get_cmap("plasma").colors
# palette = denormalize(colormap)


mandelbrot_set = MandelbrotSet(max_iterations=max_iterations, escape_radius=escape_radius)
image = Image.new(mode="RGB", size = (sizeX, sizeY))
viewport = Viewport(image, center=center, width=width)
paint(mandelbrot_set, viewport, palette, smooth=True)


image.show()
