import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test():
    print("NumPy version:", np.__version__)
    print("Pandas version:", pd.__version__)
    print("Matplotlib installed successfully")

    x = np.array([1, 2, 3, 4])
    y = np.array([10, 20, 25, 30])

    plt.plot(x, y)
    plt.show()

test()