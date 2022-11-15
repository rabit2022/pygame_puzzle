# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""

import sys

import pygame
from pygame.locals import *

from settings import Setting


class UiEvent(object):
    def __init__(self, ui, *button):
        self.ui = ui

        self.buttons = button

        # self.finish = self.game.finish

        self.settings = Setting()

        self.screen_rect = self.ui.windowSurface.get_rect()

        self.option_button = self.buttons[3]
        # 按键4的锁
        self.button_lock_4 = True

    def check_events(self):
        """
        在玩家单击Play按钮时开始新游戏
        :return:
        """
        for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                # 退出
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                # 重新开始
                self.ui.universal_events(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # 玩家用鼠标单击Play按钮时作出响应
                self.mousedown_event()

    def mousedown_event(self):
        # get_pos()，它返回一个元组，其中包含玩家单击时鼠标的x和y坐标
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        if self.settings.PAUSE_GAME:  # 点击，游戏暂停时生效
            # 使用collidepoint()检查鼠标单击位置是否在Play按钮的rect内
            if self.button_collide(self.buttons[0]):
                self.cell_create(3)

            if self.button_collide(self.buttons[1]):
                self.cell_create(4)

            if self.button_collide(self.buttons[2]):
                self.cell_create(6)

            if self.button_collide(self.buttons[3]) and self.button_lock_4 == True:
                self.option_button = self.buttons[4]
                self.button_lock_4 = False
            elif self.button_collide(self.buttons[4]) and self.button_lock_4 == False:
                self.option_button = self.buttons[3]
                self.button_lock_4 = True

    def button_collide(self, buttonObj):
        return buttonObj.button_rect.collidepoint(self.mouse_x, self.mouse_y)

    def cell_create(self, size):
        # 开始游戏
        self.settings.PAUSE_GAME = False
        self.settings.VHNUMS = size
