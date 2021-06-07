from BLOCK import MINO
from DATA import *
import tkinter as tk
from UI import Window
from random import randint
import numpy as np


class GameManager:
    def __init__(self):
        self.window = Window()
        self.field = self.window.gamefield
        self.color = np.full((FIELD_HEIGHT, FIELD_WIDTH), "gray70", dtype='U13')
        self.next = self.window.nextfield
        self.mino = None

    def set_colorlist(self, x, y, color):
        self.color[y][x] = color

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

    def can_rotate(self, direction) -> bool:
        mino_verify = self.mino.copy()
        mino_verify.rotate(direction)
        shape_varify = mino_verify.get_shape()
        coord_varify = mino_verify.get_coordinates()
        move_status = 0

        for y in range(len(shape_varify)):
            for x in range(len(shape_varify[y])):

                # ミノが存在する場所の判定
                if shape_varify[y][x] == 0:
                    continue
                elif shape_varify[y][x] == 1:
                    x_verify = x+coord_varify[0]
                    y_verify = y+coord_varify[1]

                    # フィールドからはみ出す場合
                    if (x_verify < 0) or (x_verify > FIELD_WIDTH):
                        print("MINO cannnot rotate in this direction")
                        return False, move_status
                    elif (y_verify < 0) or (y_verify >= FIELD_HEIGHT):
                        print("MINO cannnot rotate in this direction")
                        return False, move_status

                    # 右端での回転処理
                    elif x_verify == FIELD_WIDTH:
                        move_status = 1

                    # すでにブロックがある場合
                    elif self.color[y_verify][x_verify] != "gray70":
                        print("MINO cannnot rotate in this direction")
                        return False, move_status


                    # 何でもない場合、次の座標の検証に進む
                    else:
                        continue
        return True, move_status

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

    def rotate_left(self):
        canrotate, condition = self.can_rotate(LEFT)
        if canrotate is True:
            self.mino.rotate(LEFT)
            if condition == 1:
                self.mino.move(LEFT)
            self.field.display(self.color)
            self.field.draw_mino(mino=self.mino)
        else:
            pass

    def rotate_right(self):
        canrotate, condition = self.can_rotate(RIGHT)
        if canrotate is True:
            self.mino.rotate(RIGHT)
            if condition == 1:
                self.mino.move(LEFT)
            self.field.display(self.color)
            self.field.draw_mino(mino=self.mino)
        else:
            pass

    def delete_line(self):
        for j in range(FIELD_HEIGHT):
            if "gray70" not in self.color[j]:
                temp = np.delete(self.color, j, 0) # j行目を削除
                topline = np.array(["gray70"]*FIELD_WIDTH, dtype='U13') # 挿入する空白行
                self.color = np.insert(temp, 0, topline, axis=0) #空白行を挿入
            else:
                pass

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
        self.delete_line()
        self.make_new_mino()


class EventHandller:
    def __init__(self, master, game:GameManager):
        self.master = master
        self.game = game
        button_start = tk.Button(text="START", command=self.start)
        button_start.place(x=25+BLOCK_SIZE*(FIELD_WIDTH+7), y=60)


    def start(self):
        self.game.make_new_mino()

        """key入力の受付開始"""
        """
        self.master.bind("<Left>", self.left_key_event)
        self.master.bind("<Right>", self.right_key_event)
        self.master.bind("<Down>", self.down_key_event)
        """
        self.master.bind("<a>", self.left_key_event)
        self.master.bind("<d>", self.right_key_event)
        self.master.bind("<s>", self.down_key_event)
        self.master.bind("<Button-1>", self.left_click_event)
        self.master.bind("<Button-3>", self.right_click_event)
        self.timer()

    def timer(self):
        self.master.after(1000, self.time_event)

    def left_key_event(self, event):
        self.game.move_left()

    def right_key_event(self, event):
        self.game.move_right()

    def down_key_event(self, event):
        self.game.move_down()

    def left_click_event(self, event):
        self.game.rotate_left()

    def right_click_event(self, event):
        self.game.rotate_right()

    def time_event(self):
        self.game.move_down()
        self.timer()
