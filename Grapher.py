"""Generate a 2d graph object for displaying (x,y) data as text"""


class Grapher:
    """Generate a 2d graph object for displaying (x,y) data as text.

    Args:
        height (int): Number of vertical positions.
        width (int): Number of horizontal positions.
        init_x (int): Optional. 0 reference offset from left edge.
        init_y (int): Optional. 0 reference offset from bottom edge.
        fill (str): Optional. Character to fill each position in grid. Default is ".". 
    """

    def __init__(self, height=10, width=10, init_x=0, init_y=0, fill="."):
        self.height = height
        self.width = width
        self.init_x = init_x
        self.init_y = init_y
        self.fill = fill
        self.graph = self._generate_graph()

    def _generate_graph(self) -> list[list[str]]:
        """Generate a graph with the specified dimensions.

        Returns:
            list[list[str]]: A list of rows of positions in the graph.
        """
        return [[self.fill for _ in range(self.width)]
                for _ in range(self.height)]

    def set_value(self, x, y, value):
        """Set value at a specified position to item, usually str or int.

        Args:
            x (int): Horizontal coordinate to set.
            y (int): Vertical coordinate to set.
            item (str or int): Value, usually str or int, to set at position.
        """
        x, y = self._transpose(x, y)
        self.graph[x][y] = value

    def get_value(self, x, y):
        """Get value at position.

        Args:
            x (int): Horizontal coordinate to get.
            y (int): Vertical coordinate to get.

        Returns:
            str or int: Value of object from specified position.
        """
        x, y = self._transpose(x, y)
        return self.graph[x][y]

    def _transpose(self, x, y) -> tuple:
        """Convert x,y coordinates to i,j type tuple for use in a subscriptable
        nested loop. (list of lists) 

        X values increase to the right like nested j values do. 
        X values increase upwards which is opposite to i in general.
        The x,y starting position is lower-left by default. i,j is upper-left.

        Args:
            x (int): Horizontal coordinate to convert.
            y (int): Vertical coordinate to convert.

        Returns:
            tuple: (i,j) Position reference for use in a subscriptable nested loop. 
        """
        return (
            [n for n in range(self.height)][::-1][y + self.init_y],
            x + self.init_x,
        )

    def display(self) -> str:
        """Convert graph list to printable string.

        Returns:
            str: An easily printable block string.
        """
        # Convert any non-str items to str
        graph_list = [[str(item) for item in line] for line in self.graph]
        # Return printable 2d str
        return "\n".join(["".join(line) for line in graph_list])
