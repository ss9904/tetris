import tkinter as tk
from DATA import *
from BLOCK import *


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
        self.nextfield.place(x=25+BLOCK_SIZE*(FIELD_WIDTH+2), y=50)

    def draw_mino(self):
        self.gamefield.draw_mino()


class GameField(tk.Canvas):
    """
    テトリミノが積みあがる画面
    """

    def __init__(self):

        canvas_width = BLOCK_SIZE * FIELD_WIDTH
        canvas_height = BLOCK_SIZE * FIELD_HEIGHT

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

    def display(self, colorlist):
        """リストから盤面を塗りなおすメソッド"""
        for y in range(FIELD_HEIGHT):
            for x in range(FIELD_WIDTH):
                x0 = x*BLOCK_SIZE
                y0 = y*BLOCK_SIZE
                x1 = (x+1)*BLOCK_SIZE
                y1 = (y+1)*BLOCK_SIZE

                self.create_rectangle(
                    x0, y0, x1, y1, fill=COLORS[colorlist[y][x]],
                    outline="white", width=1
                )

    def update_color(self, x, y, color):
        """指定の座標を指定の色に塗り替えるメソッド"""
        x0 = x*BLOCK_SIZE
        y0 = y*BLOCK_SIZE
        x1 = (x+1)*BLOCK_SIZE
        y1 = (y+1)*BLOCK_SIZE
        color = COLORS[color]

        self.create_rectangle(
            x0, y0, x1, y1, fill=color,
            outline="white", width=1
        )

    def draw_mino(self, mino:MINO):
        """
        管理しているミノを描画するメソッド
        色,形,座標はミノ自身が保持している
        """
        coord = mino.get_coordinates()
        shape = mino.get_shape()
        color = COLORS[mino.get_color()]

        for j in range(len(shape)):
            for i in range(len(shape[j])):
                if shape[j][i] == 0:
                    continue
                else:
                    self.update_color(coord[0]+i, coord[1]+j, color)


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

    def draw_mino(self, mino:MINO):
        """
        管理しているミノを描画するメソッド
        色,形,座標はミノ自身が保持している
        """
        shape = mino.get_shape()
        color = mino.get_color()

        for y in range(4):
            for x in range(3):
                if shape[y][x] == 0:
                    x0 = x*BLOCK_SIZE
                    y0 = y*BLOCK_SIZE
                    x1 = (x+1)*BLOCK_SIZE
                    y1 = (y+1)*BLOCK_SIZE

                    self.create_rectangle(
                        x0, y0, x1, y1, fill="gray70",
                        outline="white", width=1
                    )
                else:
                    x0 = x*BLOCK_SIZE
                    y0 = y*BLOCK_SIZE
                    x1 = (x+1)*BLOCK_SIZE
                    y1 = (y+1)*BLOCK_SIZE

                    self.create_rectangle(
                        x0, y0, x1, y1, fill=color,
                        outline="white", width=1
                    )
