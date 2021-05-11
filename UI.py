import tkinter as tk
from TETRIMINOdata import *
from BLOCK import MINO
from random import randint


class Window(tk.Frame):
    """
    ゲームウィンドウのクラス
    """

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.master.geometry("600x800")
        self.master.title("test")

        self.gamefield = GameField()
        self.gamefield.place(x=25, y=50)

        self.nextfield = NextField()
        self.nextfield.place(x=300, y=50)

    def draw_mino(self, mino):
        self.gamefield.draw_mino(mino)


class GameField(tk.Canvas):
    """
    テトリミノが積みあがる画面
    """

    def __init__(self):

        canvas_width = BLOCK_SIZE * FIELD_WIDTH
        canvas_height = BLOCK_SIZE * FIELD_HEIGHT

        # 盤面の状態を記憶するリスト
        self.color = [["gray70"]*FIELD_WIDTH]*FIELD_HEIGHT

        tk.Canvas.__init__(
            self, master=None,
            width=canvas_width, height=canvas_height,
            )

        for y in range(FIELD_HEIGHT):
            for x in range(FIELD_WIDTH):
                x0 = x*BLOCK_SIZE
                y0 = y*BLOCK_SIZE
                x1 = (x+1)*BLOCK_SIZE
                y1 = (y+1)*BLOCK_SIZE

                self.create_rectangle(
                    x0, y0, x1, y1, fill="gray70",
                    outline="white", width=1
                )

    def overwrite_color(self, x, y, color):
        """リストの更新"""
        self.color[y][x] = color

    def reset_color(self):
        for y in range(FIELD_HEIGHT):
            for x in range(FIELD_WIDTH):
                x0 = x*BLOCK_SIZE
                y0 = y*BLOCK_SIZE
                x1 = (x+1)*BLOCK_SIZE
                y1 = (y+1)*BLOCK_SIZE

                self.create_rectangle(
                    x0, y0, x1, y1, fill=self.color[y][x],
                    outline="white", width=1
                )

    def update_color(self, x, y, color):
        x0 = x*BLOCK_SIZE
        y0 = y*BLOCK_SIZE
        x1 = (x+1)*BLOCK_SIZE
        y1 = (y+1)*BLOCK_SIZE

        self.create_rectangle(
            x0, y0, x1, y1, fill=color,
            outline="white", width=1
        )

    def draw_mino(self, MINO:MINO):
        coord = MINO.get_coordinates()
        shape = MINO.get_shape()
        color = MINO.get_color()

        self.reset_color()

        for j in range(len(MINO.shape)):
            for i in range(len(MINO.shape[j])):
                if shape[j][i] == 0:
                    continue
                else:
                    self.update_color(i+coord[0], j+coord[1], color)


class NextField(tk.Canvas):
    """Next表示エリア"""

    def __init__(self):

        canvas_width = BLOCK_SIZE*3 - 1 #(なぜか1引いたほうがきれいに描画されるので)
        canvas_height = BLOCK_SIZE*4 - 1 #(とりあえず1引いておく)

        tk.Canvas.__init__(
            self, master=None,
            width=canvas_width, height=canvas_height,
            )

        for y in range(canvas_width):
            for x in range(canvas_height):
                x0 = x*BLOCK_SIZE
                y0 = y*BLOCK_SIZE
                x1 = (x+1)*BLOCK_SIZE
                y1 = (y+1)*BLOCK_SIZE

                self.create_rectangle(
                    x0, y0, x1, y1, fill="gray70",
                    outline="white", width=1
                )









if __name__ == "__main__":
    gameWindow = Window()

    mino = MINO(J, (0,0))

    print(mino.shape)
    mino.rotate(1)
    print(mino.shape)

    mino.set_coordinates(5,6)
    gameWindow.draw_mino(mino)

    gameWindow.mainloop()
