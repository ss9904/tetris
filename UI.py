import tkinter as tk
from tkinter.constants import NONE


# constants
BLOCK_SIZE = 25
FIELD_WIDTH = 10
FIELD_HEIGHT = 24


class Window(tk.Frame):
    """
    ゲームウィンドウのクラス
    """

    def __init__(self, master=None): # tk.Frameを好みに改造して初期化
        tk.Frame.__init__(self, master)
        
        self.master.geometry("600x800")
        self.master.title("test")


    def make_game_field(self):
        field = GameField()
        field.place(x=25, y=50)



class GameField(tk.Canvas):
    """ミノが積みあがる画面"""

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



if __name__ == "__main__":
    gameWindow = Window()
    gameWindow.make_game_field()
    gameWindow.mainloop()
