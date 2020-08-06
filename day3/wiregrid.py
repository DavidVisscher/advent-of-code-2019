"""
Advent of Code - Day 3

WireGrid module.
"""

from tqdm import tqdm


class WireGrid:
    """
    Contains the data for a simulation.
    """

    def __init__(self, size = 10000):
        """
        Creates a WireGrid
        """
        self.offset = int(size / 2)
        
        self.size = size
        self.grid = []
        self._init_grid()

    def _init_grid(self):
        """
        Initializes the grid.

        Creates an empty list in every space.
        """
        for col in tqdm(range(self.size), desc="Allocating Grid"):
            self.grid.insert(col, [])
            for row in range(self.size):
                self.grid[col].insert(row, [])

    def _offset_coordinates(self, x, y) -> tuple:
        """
        compensates coordinates for offset.
        """
        return (x + self.offset, y + self.offset)
    
    def _reverse_offset_coordinates(self, x, y) -> tuple:
        """
        compensates coordinates for offset.
        """
        return (x - self.offset, y - self.offset)

    def get(self, x, y) -> list:
        """
        Gets an item from the grid.

        Uses the inset offset to allow for negative values.
        """
        x, y = self._offset_coordinates(x, y)

        return self.grid[x][y]

    def add(self, x, y, element):
        """
        Adds an element to a position on the grid.
        """
        x, y = self._offset_coordinates(x, y)
        
        if element not in self.grid[x][y]:
            self.grid[x][y].append(element)

    def set(self, x, y, value):
        """
        sets a field in the grid.
        """
        x, y = self._offset_coordinates(x, y)
        
        self.grid[x][y] = value
    
    def clear(self, x, y, value):
        """
        sets a field in the grid.
        """
        x, y = self._offset_coordinates(x, y)
        
        self.grid[x][y] = []

    @property
    def crossings(self):
        """
        List of coordinates where wires cross.
        """
        out = []
        for col in range(self.size):
            for row in range(self.size):
                if len(self.grid[col][row]) >= 2:
                    out.append(self._reverse_offset_coordinates(col,row))
        return out
