# Grapher

A lightweight Python utility for creating ASCII text-based 2D graphs. Perfect for visualizing (x, y) data in terminal environments or simple text-based applications.

## Features

- Configurable grid dimensions and fill characters  
- Coordinate system with customizable origin offsets
- Simple API for plotting and retrieving data points
- Text-based output ideal for terminals and logs

## Installation

Copy `grapher.py` to your project directory and import the `Grapher` class.

## Quick Start

```python
from grapher import Grapher

# Create a 10x10 grid
graph = Grapher(width=10, height=10)

# Plot some points
graph.set_value(2, 3, "A")
graph.set_value(7, 8, "B")

# Display the graph
print(graph.display())
```

## Use Cases

### 1. Game Development
Create ASCII game maps and display player/object positions:

```python
from grapher import Grapher

# Create a dungeon map
dungeon = Grapher(width=12, height=8, fill=" ")

# Add walls
for x in range(12):
    dungeon.set_value(x, 0, "#")  # Bottom wall
    dungeon.set_value(x, 7, "#")  # Top wall
for y in range(8):
    dungeon.set_value(0, y, "#")  # Left wall
    dungeon.set_value(11, y, "#") # Right wall

# Add game elements
dungeon.set_value(2, 3, "@")  # Player
dungeon.set_value(8, 5, "T")  # Treasure
dungeon.set_value(5, 2, "M")  # Monster

print(dungeon.display())
```

Output:
```
############
#          #
#    M     #
#  @       #
#          #
#        T #
#          #
############
```

### 2. Data Visualization
Plot data points for simple terminal-based charts:

```python
from grapher import Grapher

# Visualize temperature readings over a week
temps = [(0, 2), (1, 5), (2, 8), (3, 6), (4, 9), (5, 7), (6, 4)]
chart = Grapher(width=7, height=10, fill=".")

# Plot temperature data
for day, temp in temps:
    chart.set_value(day, temp, "*")

# Add labels
for i in range(7):
    chart.set_value(i, 0, str(i))

print("Temperature Chart (Days 0-6):")
print(chart.display())
```

Output:
```
Temperature Chart (Days 0-6):
.......
.......
....*.
..*..*.
.*.....
.......
...*.*.
.......
.......
0123456
```

## API Reference

### Constructor
```python
Grapher(width=10, height=10, init_x=0, init_y=0, fill=".")
```
- `width`: Grid width (default: 10)
- `height`: Grid height (default: 10)  
- `init_x`: X-axis offset for coordinate (0,0) (default: 0)
- `init_y`: Y-axis offset for coordinate (0,0) (default: 0)
- `fill`: Default character for empty cells (default: ".")

### Methods
- `set_value(x, y, value)`: Place a value at coordinates (x, y)
- `get_value(x, y)`: Retrieve the value at coordinates (x, y)
- `display()`: Return the grid as a printable string
