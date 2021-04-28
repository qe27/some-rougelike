import math
import random
import time
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import tkinter as tk

from global_variables import map_width, map_height


class RandomNoise():
    """
    Random noise class to create random values in 2d array
    """

    def __init__(self, width=32, height=32, bit_depth=255, extra=32):
        self.w = width + extra
        self.h = height + extra

        self.bit_depth = bit_depth
        self.extra = extra

    def randomize(self):
        """
        Creates a random grid of w x h of values between 0-1 with precision
        determined by the bit_depth; e.g. bit_depth = 255 values can be from
        0 to 1 with 255 distinct values; 0/255, 1/255, 2/255, etc...
        """
        # self.n = [[random.randint(0, self.bit_depth) / self.bit_depth for y in range(self.h)] for x in range(self.w)]
        noise = PerlinNoise(octaves=1.5, seed=2)
        # random_noise_obj.n
        # xpix, ypix = random_noise_obj.w, random_noise_obj.h
        self.n = [[abs(noise([i/32, j/32])) for j in range(self.h)] for i in range(self.w)]



        # plt.imshow(pic, cmap='gray')
        # plt.show()

    def noise2d(self, x, y):
        """
        Returns a certain value from the randomized grid.
        """
        return self.n[x][y]

    def smoothNoise2d(self, bit_depth=255, smoothing_passes=15, upper_value_limit=1):
        """
        Smooths the random grid and returns the smoothed noise values
        """
        # If not enough grid size
        if self.extra < smoothing_passes:
            print(
                "Warning, to maintain intial grid, call the RandomNoise object with a larger 'extra' value; i.e. RandomNoise(extra=your_extra)")
            self.extra = smoothing_passes
            self.__init__(extra=smoothing_passes)
            self.randomize()

        # Convert the grid to values between 0 and the upper_value_limit
        values = [[upper_value_limit * self.noise2d(x, y) for y in range(self.h - self.extra + smoothing_passes)] for x
                  in range(self.w - self.extra + smoothing_passes)]

        # Smoothing the random grid
        for _pass in range(smoothing_passes):
            self.largest_delta = float(max(map(max, values)) - min(map(min, values))) ** 2
            values = [
                [((values[x][y] + values[x + 1][y] + values[x][y + 1] + values[x - 1][y] + values[x][y - 1]) / 5) for y
                 in range(len(values[x]) - 1)] for x in range(len(values) - 1)]

        return values


# random_noise_obj = RandomNoise(32, 32, bit_depth=255, extra=40)  # 32x32 grid, bitdepth
# random_noise_obj.randomize()

"""
CANVAS EXAMPLE
"""


def render(smoothing_passes, random_noise_obj, water_amount, sand_amount, land_amount, LAND=False):
    p = smoothing_passes
    sq = 10
    colours = random_noise_obj.smoothNoise2d(smoothing_passes=p)

    for x in range(0, len(colours)):
        for y in range(0, len(colours[x])):
            col = int(colours[x][y] * 255)
            if LAND:
                if col in range(0, int(255 * water_amount)):  # water
                    final = '#%02X%02X%02X' % (0, 0, col)
                elif col in range(int(255 * (water_amount)), int(255 * (water_amount + sand_amount))):  # sand
                    final = '#%02X%02X%02X' % (col, col, 0)
                elif col in range(int(255 * (water_amount + sand_amount)),
                                  int(255 * (water_amount + sand_amount + land_amount))):  # land
                    final = '#%02X%02X%02X' % (0, col, 0)
                elif col in range(int(255 * (water_amount + sand_amount + land_amount)), 255):  # mountain
                    final = '#%02X%02X%02X' % (col, col, col)
                else:
                    final = '#%02X%02X%02X' % (col, col, col)
            else:
                final = '#%02X%02X%02X' % (col, col, col)
            # canvas.create_rectangle(x * sq, y * sq, (x * sq) + sq, (y * sq) + sq, fill=final, width=0,
            #                         tags=("RCT" + str(p)))

        # if x % 10 == 0:
        #     root.update()
        # canvas.delete("RCT" + str(p - 1 - (step % 2)))
    # root.update()


def generate_random_map_values():
    # root = tk.Tk()
    # w = int(root.winfo_screenwidth() // 1.5)
    # h = int(root.winfo_screenheight() // 1.5)
    sq = 10
    FPS = 10
    smoothing_passes = 1

    random_noise_obj = RandomNoise(map_width, map_height, 255, smoothing_passes)
    random_noise_obj.randomize()

    # canvas = tk.Canvas(root, height=h, width=w, bg="black", highlightthickness=0)
    # canvas.pack()

    # smoothingl = tk.Label(root, text="Size: {}x{} | Smoothing pass: {}/{}".format(w // sq, h // sq, 0, smoothing_passes))
    # smoothingl.pack()

    # fraction of 1.0
    water_amount = 0.18
    sand_amount = 0.03
    land_amount = 0.7

    print("water_range", 0, int(255 * water_amount))
    print("sand_range", int(255 * (water_amount)), int(255 * (water_amount + sand_amount)))
    print("land_range", int(255 * (water_amount + sand_amount)), int(255 * (water_amount + sand_amount + land_amount)))
    print("mountain_range", int(255 * (water_amount + sand_amount + land_amount)), 255)

    random_noise_obj.randomize()
    step = 1
    for p in range(0, smoothing_passes, step):
        render(p, random_noise_obj, water_amount, sand_amount, land_amount, True)
        # smoothingl.config(text="Size: {}x{} | Smoothing pass: {}/{}".format(w // sq, h // sq, p + 1, smoothing_passes))

        # time.sleep(1 / FPS)

    # render(smoothing_passes)

    # root.mainloop()
    return random_noise_obj

# generate_random_map_values()