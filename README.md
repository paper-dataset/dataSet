This dataset is used for anonymous review.

The dataset comes from 2800 CAN signals collected on the CAN bus. After careful sorting, we divided them into normal signals and abnormal signals. Normal signals include 2400 signals from 8 benign devices on the CAN bus. The abnormal signals include 400, each from signals from intrusion devices in eight attack scenarios. 

The dataset is in npy file format, so it is an array saved in Python using the NumPy library. An npy file is a binary file format used to store a single NumPy array. Here is a descriptive example of how to load npy file data:
Step 1: You need to ensure that the NumPy library is installed in your Python environment. If it has not been installed yet, you can use pip (Python's package manager) to install it;
Step 2: Once the NumPy library is installed, you can use its load function to load data from the. npy file. This function will read the file and return its contents as a NumPy array.
Please note that the npy file only contains a single NumPy array and does not contain metadata such as column names or data types.

For more information, please refer to the paper “PIL-MDRS: Physical Intrusion Localization based on Multi-Device Reflection Signals in ICS”
