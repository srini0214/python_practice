1. Why AI Debugging is Harder
In standard software, a bug is usually "Variable X is null." In AI:

Non-determinism: The model might work on Monday and fail on Tuesday with the same input.

Opaque Data: You aren't just checking an integer; you're checking a 1×4096 hidden state tensor.

Async Messiness: When an async function fails, the stack trace can look like a nightmare of internal Python loop code.



2. Tool #1: The VS Code Debugger (Visual Flow)
If you aren't using the Run and Debug tab in VS Code, you're debugging with one eye closed.

Conditional Breakpoints: Don't stop every time. Right-click a breakpoint and set an expression like len(tokens) > 500. Only stop when the data is "heavy."

The "Watch" Window: Keep an eye on your Pydantic objects. As the LLM streams data, you can watch the BugReport object fill up in real-time.

The Debug Console: This is a live Python REPL. While the code is paused at a breakpoint, you can run model.predict(test_data) to see what would happen without restarting the script.

3. Tool #2: breakpoint() and pdb
Sometimes you're debugging on a remote server (like a GPU cluster) where you don't have a GUI.

Simply drop breakpoint() anywhere in your code. When Python hits that line, it will drop you into the PDB (Python Debugger) terminal.

Essential PDB Commands:

n (next): Execute the next line.

s (step): Step into a function call.

c (continue): Run until the next breakpoint.

p variable_name: Print the value of a variable.

ll (long list): See the source code around your current position.

4. Inspecting the "AI State"
When working with models (PyTorch) or structured data (Pydantic), "printing" isn't enough. Use these three commands in your debugger:

type(obj): Is this a list, or is it a numpy.ndarray? (Crucial for data pipelines).

obj.shape: (For Tensors/Arrays). If your model expects 768 dimensions and you give it 512, it will crash.

obj.dict(): (For Pydantic). Quickly see the entire state of your validated data as a clean dictionary.
