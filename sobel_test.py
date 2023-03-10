import numpy as np
import matplotlib.pyplot as plt
import pylab
A = np.array([[200, 66, 55], [99, 88, 45], [100, 54, 60]])
plt.imshow(A, cmap=plt.get_cmap('gray'))
plt.show()
Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
GxA, GyA = np.sum(np.multiply(Gx, A)), np.sum(np.multiply(Gy, A))
# equal to the "hypotenuse" of the values in the x and y directions
output_value = np.sqrt(GxA**2 + GyA**2)
print("output pixel value =", output_value)
