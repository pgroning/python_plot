import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100)

k = 0.04
#y = 100 * (1 - np.exp(-k * x))
y = (2 / (1 + np.exp(-k*x)) - 1) * 100
#y = np.log(x+1)
print y
#y = map(int, y)

plt.plot(x, y)
plt.show()
