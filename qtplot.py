import matplotlib as mpl
mpl.use("qt4Agg")  # Use Qt4 graphics library

import matplotlib.pyplot as plt
import numpy as np

def plot():
    
    mpl.rcParams["lines.linewidth"] = 2

    x = np.linspace(-10,10,100)
    y = np.sin(x)/x
    
    plt.plot(x, y)
    plt.ylabel("sin(x)/x")
    plt.show()


if __name__ == "__main__":
    plot()
