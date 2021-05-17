import tkinter as tk
from DATA import *
from random import randint
from BLOCK import MINO
from UI import Window


class GameManager:
    def __init__(self):
        self.window = Window()
        self.field = self.window.gamefield
        self.color = [["gray70"]*FIELD_WIDTH for i in range(FIELD_HEIGHT)]
        self.next = self.window.nextfield
        self.mino = None

    def set_colorlist(self, x, y, color):
        print(self.color[y][x], x, y, type(self.color[y][x]))
        self.color[y][x] = str(color)

    def make_new_mino(self):
        self.mino = MINO(mino_name=TETRIMINOS[randint(0,6)])
        self.field.draw_mino(mino=self.mino)

    def can_move(self, direction) -> bool:
        mino_verify = self.mino.copy()
        mino_verify.move(direction)
        shape_varify = mino_verify.get_shape()
        coord_varify = mino_verify.get_coordinates()

        for y in range(len(shape_varify)):
            for x in range(len(shape_varify[y])):

                # ミノが存在する場所の判定
                if shape_varify[y][x] == 0:
                    continue
                elif shape_varify[y][x] == 1:
                    x_verify = x+coord_varify[0]
                    y_verify = y+coord_varify[1]

                    # フィールドからはみ出す場合
                    if (x_verify < 0) or (x_verify >= FIELD_WIDTH):
                        print("MINO cannnot move in this direction")
                        return False
                    elif (y_verify < 0) or (y_verify >= FIELD_HEIGHT):
                        print("MINO cannnot move in this direction")
                        return False

                    # すでにブロックがある場合
                    elif self.color[y_verify][x_verify] != "gray70":
                        print("MINO cannnot move in this direction")
                        return False

                    # 何でもない場合、次の座標の検証に進む
                    else:
                        continue
        return True

    def move_left(self):
        if self.can_move(LEFT) is True:
            self.mino.move(LEFT)
            self.field.display(self.color)
            self.field.draw_mino(mino=self.mino)
        else:
            pass

    def move_right(self):
        if self.can_move(RIGHT) is True:
            self.mino.move(RIGHT)
            self.field.display(self.color)
            self.field.draw_mino(mino=self.mino)
        else:
            pass

    def move_down(self):
        if self.can_move(DOWN) is True:
            self.mino.move(DOWN)
            self.field.display(self.color)
            self.field.draw_mino(mino=self.mino)
        else:
            self.fix_mino()
            self.delete_line()
            self.make_new_mino()

    def fix_mino(self):
        shape = self.mino.get_shape()
        coord = self.mino.get_coordinates()
        color = self.mino.get_color()

        for j in range(len(shape)):
            for i in range(len(shape[j])):
                if shape[j][i] == 0:
                    continue
                else:
                    self.set_colorlist(x=coord[0]+i, y=coord[1]+j, color=color)


        del self.mino

    def delete_line(self):
        for j in range(FIELD_HEIGHT):
            if self.color[j].count("gray70") == 0:
                del self.color[j]
                self.color.insert(0, ["gray70"]*FIELD_WIDTH)
            else:
                pass


class EventHandller:
    def __init__(self, master, game:GameManager):
        self.master = master
        self.game = game
        start_buton = tk.Button(text="START", command=self.start)
        start_buton.place(x=25+BLOCK_SIZE*(FIELD_WIDTH+7), y=60)


    def start(self):
        self.game.make_new_mino()

        """key入力の受付開始"""
        self.master.bind("<Left>", self.left_key_event)
        self.master.bind("<Right>", self.right_key_event)
        self.master.bind("<Down>", self.down_key_event)


    def left_key_event(self, event):
        self.game.move_left()

    def right_key_event(self, event):
        self.game.move_right()

    def down_key_event(self, event):
        self.game.move_down()






if __name__ == "__main__":
    """
    gameWindow = Window()

    mino = MINO(J)

    print(mino.shape)
    mino.rotate_left()
    print(mino.shape)

    gameWindow.draw_mino(mino)
    """
    root = tk.Tk()
    app = GameManager()
    manage = EventHandller(root, app)
    app.window.mainloop()
