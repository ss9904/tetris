import tkinter as tk
from typing import List
from DATA import *


class MINO(tk.Canvas):
    """テトリミノ"""

    def __init__(self, mino_name, coordinate:list=[4,0]):
        canvas_width = BLOCK_SIZE*3
        canvas_height = BLOCK_SIZE*4

        self.name = str(mino_name)
        self.shape = mino_name[0]
        self.color = mino_name[1]
        self.coordinates = coordinate

        tk.Canvas.__init__(
            self, master=None,
            width=canvas_width, height=canvas_height
            )

        for y in range(4):
            for x in range(3):
                x0 = x*BLOCK_SIZE
                y0 = y*BLOCK_SIZE
                x1 = (x+1)*BLOCK_SIZE
                y1 = (y+1)*BLOCK_SIZE
                if self.shape[y][x] == 1:
                    color = self.color
                else:
                    color = "gray70"

                self.create_rectangle(
                    x0, y0, x1, y1, fill=color,
                    outline="white", width=1
                )

    def get_name(self):
        return self.name

    def get_coordinates(self) -> list:
        return self.coordinates

    def get_shape(self) -> List[List[int]]:
        return self.shape

    def get_color(self) -> str:
        return self.color

    def set_coordinates(self, x, y):
        self.coordinates = [x, y]

    def rotate_left(self):
        new_shape = [list(k) for k in zip(*self.shape)]
        new_shape = new_shape[::-1]
        self.shape = new_shape

    def rotate_right(self):
        new_shape = [list(k) for k in zip(*self.shape[::-1])]
        self.shape = new_shape

    def move_left(self):
        coord = self.get_coordinates()
        self.set_coordinates(x=coord[0]-1, y=coord[1])

    def move_right(self):
        coord = self.get_coordinates()
        coord[0] += 1
        self.set_coordinates(*coord)

    def move_down(self):
        coord = self.get_coordinates()
        coord[1] += 1
        self.set_coordinates(*coord)

    def move(self, direction):
        coord = [
            i+j for (i,j)
            in zip(self.get_coordinates(), MOVEMENT[direction])
        ]
        self.set_coordinates(*coord)