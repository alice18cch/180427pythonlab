import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(10)
print(arr)
print(arr.ndim)
print(arr.shape)

arr2 = np.arange(5, 50, 2)
print(arr2)
arr2_1 = arr2 ** 1.2 +1
print(arr2_1)

arr3_x = np.arange(10, 50, 3)
arr3_y = arr3_x * 2 + 5

arr4_x = np.linspace(0, 10, 21)
arr4_y1 = arr4_x * 2
arr4_y2 = arr4_x * 3
print(arr4_x)

#plt.plot(arr2, arr2_1, linestyle = '--', marker = 'o', color = 'r')
plt.plot(arr4_x, arr4_y1, '-rv', arr4_x, arr4_y2, '--bo')
plt.show()