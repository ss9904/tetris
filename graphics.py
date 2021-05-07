import tkinter


# constants
BLOCK_SIZE = 25
FIELD_WIDTH = 10
FIELD_HEIGHT = 24


class Window(tkinter.Tk):
    """
    ゲームウィンドウのクラス
    """

    def __init__(self,):
        super().__init__()
        
        self.geometry("600x800")
        self.title("test")


class Field(tkinter.Canvas):
    """テトリミノが積みあがる画面"""

    def __init__(self, window):

        canvas_width = BLOCK_SIZE * FIELD_WIDTH
        canvas_height = BLOCK_SIZE * FIELD_HEIGHT

        super().__init__(
            window,
            width=canvas_width,
            height=canvas_height,
            bg="cyan"
            )

        self.pack()



if __name__ == "__main__":
    gameWindow = Window()
    field = Field(gameWindow)
    gameWindow.mainloop()
