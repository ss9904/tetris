import tkinter as tk
from TETRIMINOdata import *
from TETRIMINO import MINO



class Window(tk.Frame):
    """
    ゲームウィンドウのクラス
    """

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.master.geometry("600x800")
        self.master.title("test")

    def make_game_field(self):
        field = GameField()
        field.place(x=25, y=50)

    def make_next_field(self):
        field = NextField()
        field.place(x=300, y=50)


class GameField(tk.Canvas):
    """テトリミノが積みあがる画面"""

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

    def draw_mino(self, MINO:MINO):
        posi = MINO.get_coordinates()
        self.place(x=posi[0], y=posi[1])


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
    gameWindow.make_game_field()
    gameWindow.make_next_field()
    gameWindow.mainloop()
