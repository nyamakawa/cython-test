import sys
import time
import math

from PIL import Image
import numpy as np

import affine
import affine_cy
import affine_cy2

input_path = sys.argv[1]
output_path = sys.argv[2]

im = Image.open(input_path).convert("L")
size = (im.width, im.height)
im_arr = np.asarray(im, dtype=np.uint8)
print("im_arr.shape", im_arr.shape)
im_dest = np.ndarray(im_arr.shape, dtype=np.uint8)

t = time.time()
affine.rotate(math.pi * 0.5, im_arr, im_dest)
print(" %f sec" % (time.time() - t))

t2 = time.time()
affine_cy.rotate(math.pi * 0.5, im_arr, im_dest)
print(" %f sec" % (time.time() - t2))

t3 = time.time()
affine_cy.rotate_cy(math.pi * 0.5, im_arr, im_dest)
print(" %f sec" % (time.time() - t3))

t4 = time.time()
affine_cy2.rotate(math.pi * 0.5, im_arr, im_dest)
print(" %f sec" % (time.time() - t4))

t5 = time.time()
affine_cy2.rotate_cy(math.pi * 0.5, im_arr, im_dest)
print(" %f sec" % (time.time() - t5))


im = Image.fromarray(np.uint8(im_dest), mode="L")
im.save(output_path)