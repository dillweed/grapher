# Grapher

Grapher is a Python class that generates a 2D graph object for displaying (x, y) data as text.


## Usage

To use Grapher, first import the class and create a new `Grapher` object. You can specify the height, width, initial x and y offsets, and the fill character for the graph:

```python
from grapher import Grapher

# Create a new Grapher object with the default parameters
graph = Grapher()

# Create a new Grapher object with a height of 20, width of 30, initial x offset of 5,
# initial y offset of 10, and a fill character of "-"
graph = Grapher(height=20, width=30, init_x=5, init_y=10, fill="-")
```

Once you have created a Grapher object, you can use the following methods to manipulate the graph:

`set_value(x, y, value)`: Set the value at the specified position in the graph.

`get_value(x, y)`: Get the value at the specified position in the graph.

`display()`: Return the graph as a printable string.

Here's an example of how to use these methods:

```
# Set the value at position (2, 3) to "X"
graph.set_value(2, 3, "X")

# Get the value at position (4, 5)
value = graph.get_value(4, 5)

# Display the graph
print(graph.display())
```
