This dataset is used for anonymous review.

The dataset comes from 2800 CAN signals collected on the CAN bus. After careful sorting, we divided them into normal signals and abnormal signals. Normal signals include 2400 signals from eight benign devices on the CAN bus. The abnormal signals include 400 signals from intrusion devices in eight attack scenarios.

The dataset is in .npy binary file format, where each data file is saved as  a `NumPy` array. Here is a descriptive example of how to load .npy file data using Python:

- **Step 1:** Please ensure that the `NumPy` library is installed in your Python environment. If it has not been installed yet, you can use `pip install numpy` to install it.

- **Step 2:** Load data from the .npy file and plot the data following `test.py`:

```shell
import numpy as np
import matplotlib.pyplot as plt

data=np.load("normal/terminal1/data (1).npy")
print(len(data))
plt.plot(data)
plt.show()
```

For more information, please refer to the paper “PIL-MDRS: Physical Intrusion Localization based on Multi-Device Reflection Signals in ICS”