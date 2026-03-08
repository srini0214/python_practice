import torch

# Exercise 2: Reshaping the Brain (Tensors)

# Models are very picky about "Shapes." If a model expects a 
# (1,512) input and you give it (512,), it will crash.

# Task: Create a PyTorch tensor with 12 elements: t = torch.arange(12).
t = torch.arange(12)
print("Original tensor:", t)
print("Original shape:", t.shape)  # torch.Size([12])

# Task: Use .view(3, 4) and .view(2, 6) to reshape it.
t_3x4 = t.view(3, 4)
print("Reshaped to (3, 4):")
print(t_3x4)
print("Shape:", t_3x4.shape)  # torch.Size([3, 4])

t_2x6 = t.view(2, 6)
print("Reshaped to (2, 6):")
print(t_2x6)
print("Shape:", t_2x6.shape)  # torch.Size([2, 6])

# Question: What happens if you try .view(5, 5)? Why?
try:
    t_5x5 = t.view(5, 5)
except RuntimeError as e:
    print("Error when trying .view(5, 5):", e)

#.view(5, 5) fails: your tensor has 12 elements, but a (5, 5) 
# shape would need 25 elements, so PyTorch raises a RuntimeError 
# because the number of elements doesn’t match    