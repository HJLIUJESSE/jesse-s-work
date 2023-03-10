import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('messageImage_1666164405251.jpg')
h, w, ch = img.shape
print(h, w, ch)
# Color conversion (The OpenCV default color format is BGR)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# cv2.imwrite('input_r.png', rgb[:, :, 0])
# cv2.imwrite('input_g.png', rgb[:, :, 1])
# cv2.imwrite('input_b.png', rgb[:, :, 2])
# cv2.imwrite('input_y.png', yuv[:, :, 0])

# plot image with matplotlib
plt.figure(0)
plt.imshow(rgb)
plt.figure(1)
plt.imshow(yuv[:, :, 0], cmap='gray')
plt.show()
