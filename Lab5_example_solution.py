#an example solution for a data list of len 10

import random
import numpy as np
import matplotlib.pyplot as plt

data = [random.random() for i in range(0,10)]

x = range(0,10)

p = np.polyfit(x, data, deg=2)
y = np.polyval(p, x)


#print our coefficients
print(f"our coeffs: {p}")

plt.plot(x,data)
plt.plot(x,y)
plt.show()

#write your code here
