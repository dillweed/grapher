# Grapher

Grapher is a Python class that generates a 2D graph object for displaying (x, y) data as text.

## Usage

To use Grapher, first import the class and create a new `Grapher` object. You
can specify the width, height, initial x and y offsets, and the fill character for the
graph:

```python
from grapher import Grapher

# Create a new Grapher object with the default parameters
graph = Grapher()

# Create a new Grapher object with a height of 20, width of 30, and a fill character of space " ".
graph_spaces = Grapher(width=30, height=20, fill=" ")
```

Once you have created a Grapher object, you can use the following methods to manipulate the graph:

`set_value(x, y, value)`: Set the value at the specified position in the graph.

`get_value(x, y)`: Get the value at the specified position in the graph.

`display()`: Return the graph as a printable string.

Here's an example of how to use these methods:

```python
# Generate a graph object with optional offset
width, height = 10, 5
start_x, start_y = width // 2, height // 2
graph = Grapher(width, height, start_x, start_y)

# Create a coordinate variable with a representative character
face = (0, 0, "X")

# Set the variable in the graph
graph.set_value(*face)

# Print the graph
print(graph.display())

# Get a specific value from the graph
print(graph.get_value(0, 0))

```

Output:

```
..........
..........
.....X....
..........
..........
X
```
