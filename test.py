import numpy as np
import matplotlib.pyplot as plt

data=np.load("normal/terminal1/data (1).npy")
print(len(data))
plt.plot(data)
plt.show()