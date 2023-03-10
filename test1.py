import numpy as np
import cmath as cm
import math as ma
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 1000)
[X, Y] = np.meshgrid(x, x)
theta = np.zeros((1000, 1000))
r = np.zeros((1000, 1000))
for i in range(0, 999, 1):
    for j in range(0, 999, 1):
        [r[i, j], theta[i, j]] = cm.polar(complex(X[i, j], Y[i, j]))

idx = r <= 1
plt.imshow(idx, cmap='gray')
plt.show()
# print(theta)
