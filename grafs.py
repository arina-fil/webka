from matplotlib import pyplot as plt 
import numpy as np
a=2
b=-3
x = np.linspace(0.3,0.7,100)


plt.plot(x, a * np.log2(x))
plt.plot(x, a * np.pow(x, 2) + b)
plt.show()

x = np.linspace(10, 100,100)
plt.plot(x, a * np.log2(x))
plt.plot(x, a * np.pow(x, 2) + b)
plt.show()

