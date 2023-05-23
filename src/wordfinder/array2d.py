# Basic 2D array data structure
from typing import Any

class Array2DException(Exception):
    pass

class Array2D:
    """ A class to provide 2D array-like functionality

    Attributes:
        width (int): Describes the 2D array row-size(width) 
        height (int):Describes the 2D array column-size(height) 
    """
    def __init__(self, width:int, height:int):
        """
        Array initialization that relies on array2ds.reset.

        Args:
            width (int): Indicates the size of each 'row'
            height (int): Indicates the size of each 'column'
        """

        self.reset(width, height)

    def reset(self, width:int, height:int):
        """Resets the 2D array

        Creates a list where list-length =  width x height. The list is
        initialized to None. Width and height are stored as array2d.attributes.

        Args:
            width (int): Indicates the size of each 'row'
            height (int): Indicates the size of each 'column'
        """
        self.width = width
        self.height = height

        # Create a list of Nones; list length is array dimensions
        self.array_2d = [None] * (width * height)


    def set_at(self, val:Any, x:int, y:int):
        """
        Sets (val)ue in the array at position (x,y)

        Args:
            val (any): The value to store
            x (int): index value that must be less than array2d.height
            y (int): index value that must be less than array2d.width
        
        Raises:
            Array2DException: Thrown when X or Y exceed width/height bounds
        """

        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            xybounds = f"X: {x} Y: {y} -- H: 0 to {self.width}"\
                       f"W: 0 to {self.height}"
            raise Array2DException(f"X or Y outside of bounds: {xybounds}")
        
        ndx = (y * self.width) + x
        self.array_2d[ndx] = val


    def get_at(self, x:int, y:int) -> Any:
        """
        Gets the (val)ue in the array at position (x,y)

        Args:
            x (int): index value that must be less than array2d.height
            y (int): index value that must be less than array2d.width

        Returns:
            Any: The value stored at (x,y); May be None
        
        Raises:
            Array2DException: Thrown when X or Y exceed width/height bounds
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            xybounds = f"X: {x} Y: {y} -- H: 0 to {self.width}"\
                       f"W: 0 to {self.height}"
            raise Array2DException(f"X or Y outside of bounds: {xybounds}")

        ndx = (y * self.width) + x
        return self.array_2d[ndx] 
