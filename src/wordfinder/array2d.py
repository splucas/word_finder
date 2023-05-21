# Basic 2D array data structure
from typing import Any

class Array2DException(Exception):
    pass

class Array2D:
    def __init__(self, width:int = 8, height:int = 8):
        self.resize(width, height)

    def resize(self, width:int, height:int):
        self.width = width
        self.height = height

        # Create a list of Nones; list length is array dimensions
        self.array_2d = [None] * (width * height)

    def set_at(self, val:Any, x:int, y:int):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            xybounds = f"X: {x} Y: {y} -- H: 0 to {self.width}"\
                       f"W: 0 to {self.height}"
            raise Array2DException(f"X or Y outside of bounds: {xybounds}")
        
        ndx = (y * self.width) + x
        self.array_2d[ndx] = val


    def get_at(self, x:int, y:int) -> Any:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            xybounds = f"X: {x} Y: {y} -- H: 0 to {self.width}"\
                       f"W: 0 to {self.height}"
            raise Array2DException(f"X or Y outside of bounds: {xybounds}")

        ndx = (y * self.width) + x
        return self.array_2d[ndx] 
