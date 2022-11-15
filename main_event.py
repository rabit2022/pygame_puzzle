import sys

import pygame
from pygame.locals import *

from direction import Direction
from settings import Setting


class MainEvent(object):
    def __init__(self, game):
        self.game = game

        self.blackCell = self.game.blackCell
        self.gameBoard = self.game.gameBoard
        self.cellWidth = self.game.cellWidth
        self.cellHeight = self.game.cellHeight

        self.move = self.game.move
        self.universal_events = self.game.universal_events

        self.settings = Setting()
        self.direct = Direction(self.settings.VHNUMS, self.settings.VHNUMS)

    def check_events(self):
        """
        键盘事件检测
        :return:
        """
        for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                # 退出
                pygame.quit()
                sys.exit()

            # 上一次的slice
            self.past = self.blackCell

            if event.type == KEYDOWN:
                self.keydown_event(event)

            if event.type == MOUSEBUTTONDOWN:  # and event.button_1 == 1
                self.mousedown_event(event)

    def click_count(self):
        """
        点击次数计数
        :return:
        """
        if self.past != self.blackCell:
            self.settings.CLICKNUM += 1

    def keydown_event(self, event):
        """
        键盘按下时的检测，为了更符合实际，对移动方向作了一定的调整
        :return:
        """
        if event.key == K_LEFT or event.key == ord("a"):
            self.black_move(1)
        if event.key == K_RIGHT or event.key == ord("d"):
            self.black_move(0)
        if event.key == K_UP or event.key == ord("w"):
            self.black_move(3)
        if event.key == K_DOWN or event.key == ord("s"):
            self.black_move(2)

        # 其他通用按键
        self.universal_events(event)

    def black_move(self, direction):
        """
        格子的移动
        :return:
        """
        # 更新板子
        self.blackCell = self.move.moveTo(direction)
        # 点击次数计数
        self.click_count()

    def mousedown_event(self, event):
        """
        鼠标点击时的位置检测
        :return:
        """
        x, y = pygame.mouse.get_pos()
        col = int(x / self.cellWidth)
        row = int(y / self.cellHeight)

        next_index = col + row * self.settings.VHNUMS  # 点击的位置
        self.blackCell  # 当前位置

        if self.direct.isValiad(self.blackCell, next_index):
            # 两块板子交换
            (self.gameBoard[self.blackCell], self.gameBoard[next_index]) = (
                self.gameBoard[next_index],
                self.gameBoard[self.blackCell],
            )

            # 更新当前的索引
            self.blackCell = next_index
            self.click_count()
