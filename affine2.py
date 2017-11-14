from math import sin, cos
import numpy as np

def rotate( rad, src, dest):
    width = src.shape[1]
    height = src.shape[0]
    center_x = width / 2
    center_y = height / 2

    sin_alpha = sin(rad)
    cos_alpha = cos(rad)

    for y in range(height):
        for x in range(width):
            x_a = x - center_x
            y_a = y - center_y
            x2 = int(round(x_a * cos_alpha - y_a * sin_alpha + center_x))
            y2 = int(round(x_a * sin_alpha + y_a * cos_alpha + center_y))
            # print("x2 y2", x2, y2)

            if x2 >= 0 and x2 < width and y2 >=0 and y2 < height:
                dest[y2][x2] = src[y][x]