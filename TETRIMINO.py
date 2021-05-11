import tkinter as tk
from typing import List, Tuple
from TETRIMINOdata import *


"""
class BLOCK:
    def __init__(self, x:int, y:int, color:str):
        self.x = x
        self.y = y
        self.color = color

    def get_coordinates(self):
        return self.x, self.y

    def get_color(self):
        return self.color
"""


class MINO(tk.Canvas):
    """テトリミノ"""

    def __init__(self, mino_name, coordinate:Tuple):
        canvas_width = BLOCK_SIZE*3
        canvas_height = BLOCK_SIZE*4

        self.shape = mino_name[0]
        self.color = mino_name[1]
        self.coordinates = coordinate

        tk.Canvas.__init__(
            self, master=None,
            width=canvas_width, height=canvas_height
            )

        for y in range(3):
            for x in range(4):
                if self.shape[y][x] == 1:
                    x0 = x*BLOCK_SIZE
                    y0 = y*BLOCK_SIZE
                    x1 = (x+1)*BLOCK_SIZE
                    y1 = (y+1)*BLOCK_SIZE
                    self.create_rectangle(
                        x0, y0, x1, y1, fill=self.color,
                        outline="white", width=1
                    )
                else:
                    continue

    def get_coordinates(self) -> Tuple:
        return self.coordinates

    def get_shape(self) -> List[List[int]]:
        return self.shape

    def get_color(self) -> str:
        return self.color

    def set_coordinates(self, new_coordinates:Tuple):
        self.coordinates = new_coordinates

