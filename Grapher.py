"""Generate a 2d graph object for displaying (x,y) data"""


class Grapher:
    """Generate a 2d graph object for displaying (x,y) data

    Args:
    height (int): Number of vertical positions
    width (int): Number of horizontal positions
    init_x (int): 0 reference offset from left edge 
    init_y (int): 0 reference offset from bottom edge
    fill (str): Character to fill each position in grid. Default is "." 
    """

    def __init__(self, height=10, width=10, init_x=0, init_y=0, fill="."):
        self.height = height
        self.width = width
        self.init_x = init_x
        self.init_y = init_y
        self.fill = fill
        self.graph = self.generate()

    def generate(self) -> list[list[str]]:
        """Generate a graph sized from init arguments.

        Returns:
            list[list[str]]: List of rows of positions
        """
        block = [[self.fill for _ in range(self.width)]
                 for _ in range(self.height)]
        return block

    def set(self, _x, _y, item):
        """Set value at a specified position to item, usually str or int.

        Args:
            _x (int): x coordinate to set
            _y (int): y coordinate to set
            item (str or int): Value, usually str or int, to set at position
        """
        _x, _y = self.transpose(_x, _y)
        self.graph[_x][_y] = item

    def get(self, _x, _y):
        """Get value at position.

        Args:
            _x (int): x coordinate to get
            _y (int): y coordinate to get

        Returns:
            str or int: Value of object from specified position
        """
        _x, _y = self.transpose(_x, _y)
        return self.graph[_x][_y]

    def transpose(self, _x, _y) -> tuple:
        """Converts x,y coordinates to i,j type tuple for use in a subscriptable
        nested loop. (list of lists) 

        x values increase to the right like nested j values do. 
        y values increase upwards which is opposite to i in general.
        x,y starting position is lower-left by default. i,j is upper-left.

        Args:
            _x (int): x coordinate
            _y (int): y coordinate

        Returns:
            tuple: (i,j) Position reference for use in a subscriptable nested loop. 
        """
        return (
            [n for n in range(self.height)][::-1][_y + self.init_y],
            _x + self.init_x,
        )

    def display(self) -> str:
        """Converts graph list to printable string.

        Returns:
            str: Easily printable block string
        """
        # Convert any non-str items to str
        graph_list = [[str(item) for item in line] for line in self.graph]
        # Return printable 2d str
        return "\n".join(["".join(line) for line in graph_list])
