"""Generate a 2d graph object for displaying (x,y) data"""


class Grapher:
    """Generate a 2d graph object for displaying (x,y) data

    Args:
    height (int): Number of rows stacked in graph
    width (int): Number of columns
    init_x (int): X offset for 0 placement in 2d graph
    init_y (int): Y offset for 0 placement in 2d graph
    fill (str): Default "." Character that fills the graph
    """

    def __init__(self, height=10, width=10, init_x=0, init_y=0, fill=".") -> None:
        self.height = height
        self.width = width
        self.init_x = init_x
        self.init_y = init_y
        self.fill = fill
        self.graph = self.generate()

    def generate(self) -> list[list[str]]:
        block = [[self.fill for _ in range(self.width)] for _ in range(self.height)]
        return block

    def set(self, _x, _y, item):
        _x, _y = self.transpose(_x, _y)
        self.graph[_x][_y] = item

    def get(self, _x, _y):
        _x, _y = self.transpose(_x, _y)
        return self.graph[_x][_y]

    def transpose(self, _x, _y) -> tuple:
        """Converts x,y input coordinates to an i,j tuple for use in a nested
        loop. (list of lists)

        Args:
            _x (int): X coordinate
            _y (int): Y coordinate

        Returns:
            tuple: (i,j) coordinate for use in nested loop of iterable of iterables
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
