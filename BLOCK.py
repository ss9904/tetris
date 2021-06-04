from DATA import *
from typing import List
import numpy as np
from DATA import CENTER

class MINO():
    """テトリミノ"""

    def __init__(self, mino_name, coordinate:list=[CENTER,0]):
        self.name = mino_name
        self.shape = np.array(mino_name[0])
        self.color = mino_name[1]
        self.coordinates = coordinate

    def get_shape(self) -> List[List[int]]:
        return self.shape

    def get_color(self) -> str:
        return self.color

    def get_coordinates(self) -> list:
        return self.coordinates

    def set_coordinates(self, x, y):
        self.coordinates = [x, y]

    def __set_shape(self, newshape):
        self.shape = newshape

    """
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
    """

    def move(self, direction):
        coord = [
            i+j for (i,j)
            in zip(self.coordinates, MOVEMENT[direction])
        ]
        self.set_coordinates(*coord)

    def rotate(self, direction):
        self.__set_shape(np.rot90(self.shape, direction-1))

    def copy(self):
        return MINO((self.shape, self.color), self.coordinates)