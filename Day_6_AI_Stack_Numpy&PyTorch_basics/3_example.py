import torch
import numpy as np

# 1. Create data in NumPy (CPU)
np_data = np.random.rand(3, 3)

# 2. Convert to PyTorch Tensor
tensor_data = torch.from_numpy(np_data)

# 3. Move to GPU/Metal (MPS on Apple Silicon)
if torch.backends.mps.is_available():
    tensor_data = tensor_data.to("mps")
    print("Data is now on the Apple GPU (MPS)!")
else:
    print("MPS not available, using CPU.")