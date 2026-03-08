import torch
import numpy as np

# 1. Create data in NumPy (CPU)
np_data = np.random.rand(3, 3)

# 2. Convert to PyTorch Tensor
tensor_data = torch.from_numpy(np_data)

print("Tensor device:", tensor_data.device)

# apple silicon 
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

print(device)

# 3. Move to GPU (The Sovereign move) below is for Nvidia GPU
# if torch.cuda.is_available():
# if torch.backends.mps.is_available():
#    tensor_data = tensor_data.to("cuda")
#    print("Data is now on the GPU!")