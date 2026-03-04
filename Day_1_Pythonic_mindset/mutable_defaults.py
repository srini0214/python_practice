def add_to_batch(data, batch=None):
    if batch is None:
        batch = []
    batch.append(data)
    return batch

print(add_to_batch("Prompt 1")) # Expect: ["Prompt 1"]
print(add_to_batch("Prompt 2")) # Expect: ["Prompt 2"]