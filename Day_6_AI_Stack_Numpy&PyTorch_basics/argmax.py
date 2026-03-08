import torch

# Exercise 3: The "Argmax" (The Classifier)

# When an LLM predicts the next word, it outputs a list of probabilities 
# for every word in its vocabulary. 
# The "Argmax" is how we find the winner.

# Task: Create a tensor: probs = torch.tensor([0.1, 0.8, 0.05, 0.05]).
probs = torch.tensor([0.1, 0.8, 0.05, 0.05])

print("Probabilities:", probs)

# Task: Use torch.argmax(probs) to find the index of the highest value.
winner_index = torch.argmax(probs)

print("Index of highest probability:", winner_index.item())
print("Winning probability:", probs[winner_index].item())