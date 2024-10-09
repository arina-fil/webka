from matplotlib import pyplot as plt 
import numpy as np
plt.plot ([0,1,2,3,4,5], [0,1,4,0,16,25])
plt.plot ([0,1,2,3,4,5], [0,2,4,6,8,10])
plt.show()
ls = np.linspace(0,5,100)
plt.plot (ls,ls**2)
plt.plot(ls,2*ls)
plt.show

