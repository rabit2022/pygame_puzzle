# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""

import random

from settings import Setting


class Move(object):
    def __init__(self):
        self.settings = Setting()

        self.blackCell = self.settings.CELLNUMS - 1
        self.board = []

    def moveRight(self):
        """
        若空白图像块不在最左边，则将空白块左边的块移动到空白块位置
        :return:
        """
        if self.blackCell % self.settings.VHNUMS == 0:
            return self.blackCell
        self.board[self.blackCell - 1], self.board[self.blackCell] = (
            self.board[self.blackCell],
            self.board[self.blackCell - 1],
        )
        self.blackCell = self.blackCell - 1
        return self.blackCell

    def moveLeft(self):
        """
        若空白图像块不在最右边，则将空白块右边的块移动到空白块位置
        :return:
        """
        if self.blackCell % self.settings.VHNUMS == self.settings.VHNUMS - 1:
            return self.blackCell
        self.board[self.blackCell + 1], self.board[self.blackCell] = (
            self.board[self.blackCell],
            self.board[self.blackCell + 1],
        )
        self.blackCell = self.blackCell + 1
        return self.blackCell

    def moveDown(self):
        """
        若空白图像块不在最上边，则将空白块上边的块移动到空白块位置
        :return:
        """
        if self.blackCell < self.settings.VHNUMS:
            return self.blackCell
        (
            self.board[self.blackCell - self.settings.VHNUMS],
            self.board[self.blackCell],
        ) = (
            self.board[self.blackCell],
            self.board[self.blackCell - self.settings.VHNUMS],
        )
        self.blackCell = self.blackCell - self.settings.VHNUMS
        return self.blackCell

    def moveUp(self):
        """
        若空白图像块不在最下边，则将空白块下边的块移动到空白块位置
        :return:
        """
        if self.blackCell >= self.settings.CELLNUMS - self.settings.VHNUMS:
            return self.blackCell
        (
            self.board[self.blackCell + self.settings.VHNUMS],
            self.board[self.blackCell],
        ) = (
            self.board[self.blackCell],
            self.board[self.blackCell + self.settings.VHNUMS],
        )
        self.blackCell = self.blackCell + self.settings.VHNUMS
        return self.blackCell

    def moveTo(self, direction):
        # 适合于封装函数
        To = {
            "up": self.moveUp,
            "down": self.moveDown,
            "left": self.moveLeft,
            "right": self.moveRight,
            2: self.moveUp,
            3: self.moveDown,
            0: self.moveLeft,
            1: self.moveRight,
        }
        return To[direction]()

    def isFinished(self):
        """
        是否完成
        :return:
        """
        for i in range(self.settings.CELLNUMS - 1):
            if self.board[i] != i:
                return False
        return True

    def newGameBoard(self):
        """
        随机生成游戏盘面
        :return:
        """
        # self.board = []
        # for i in range(self.settings.CELLNUMS):
        # self.board.append(i)

        self.board = self.get_full_picture()

        self.blackCell = self.settings.CELLNUMS - 1

        self.board[self.blackCell] = -1

        self.random_move()

        # print(self.board, self.blackCell)
        return self.board, self.blackCell

    def random_move(self):
        """
        随机移动100次
        :return:
        """
        for i in range(self.settings.MAXRANDTIME):
            direction = random.randint(0, 3)
            self.black_move(direction)

    def black_move(self, direction):
        """
        格子的移动
        :return:
        """
        if direction == 0:
            self.blackCell = self.moveTo(0)
        elif direction == 1:
            self.blackCell = self.moveTo(1)
        elif direction == 2:
            self.blackCell = self.moveTo(2)
        elif direction == 3:
            self.blackCell = self.moveTo(3)

    def get_full_picture(self):
        board = []
        for i in range(self.settings.CELLNUMS):
            board.append(i)
        return board
