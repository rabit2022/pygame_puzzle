# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""
import os
import random

import pygame
from pygame.locals import *

from button import Button
from color import Color
from move import Move
from settings import Setting
from ui_event import UiEvent


class UiRun(object):
    def __init__(self):
        # 初始化
        pygame.init()

        # 计时器
        self.mainClock = pygame.time.Clock()
        # self.start = datetime.datetime.now()

        self.settings = Setting()

        # 加载图片
        self.image_dir = self.settings.IMAGE
        self.image_path = self.image_dir + random.choice(os.listdir(self.image_dir))
        print(self.image_path)

        # 图片
        self.gameImage = pygame.image.load(self.image_path)
        self.gameRect = self.gameImage.get_rect()

        # 设置窗口，窗口的宽度和高度取决于图片的宽高
        self.windowSurface = pygame.display.set_mode(
            (self.gameRect.width, self.gameRect.height)
        )
        # self.screen_rect = self.windowSurface.get_rect()

        # 标题
        pygame.display.set_caption("小小拼图")
        # 设置小图标，当前图片
        pygame.display.set_icon(self.gameImage)

        # 完成与否
        # self.finish = False

        self.move = Move()

        # UI按钮
        self.button_1 = Button(self.windowSurface, "简单", 0.5)
        self.button_2 = Button(self.windowSurface, "普通")
        self.button_3 = Button(self.windowSurface, "困难", 1.5)
        self.button_4 = Button(self.windowSurface, "时间", 1.8)
        self.button_5 = Button(self.windowSurface, "次数", 1.8)

        self.all_button = (
            self.button_1,
            self.button_2,
            self.button_3,
            self.button_4,
            self.button_5,
        )

        # 事件
        self.ui_event = UiEvent(self, *self.all_button)

        self.music_dir = self.settings.MUSIC
        self.music_path = self.music_dir + random.choice(os.listdir(self.music_dir))

        # 音乐播放
        # self.settings.music(self.music_path)

        # 背景依旧加载图片
        self.background = pygame.image.load(self.image_path)

    def ui_running(self):
        """
        ui界面
        :return:
        """

        while self.settings.PAUSE_GAME:
            # 键盘事件
            self.ui_event.check_events()

            # 背景色
            self.windowSurface.fill(Color.red.value)  # Color.red.value
            # 加载背景
            self.windowSurface.blit(self.background, (0, 0))

            # UI按钮加载
            self.all_button[0].draw_button()
            self.all_button[1].draw_button()
            self.all_button[2].draw_button()
            self.option_button = self.ui_event.option_button
            # 选项按钮
            self.option_button.draw_button()

            # 更新屏幕
            pygame.display.update()
            # 更新频率
            self.mainClock.tick(self.settings.FPS)

    def universal_events(self, event):
        """其他通用按键
        此处更换ui，不影响游戏，游戏仅仅是第一次的图片
        bug,但不好修复

        :param event:
        :return:
        """
        if event.key == K_c:
            # 重新开始游戏
            ui = UiRun()
            ui.ui_running()
        if event.key == pygame.K_z:
            # 更换音乐
            self.settings.music()

    def isButton(self, num):
        if self.option_button == self.all_button[num]:
            return True


if __name__ == "__main__":
    ui = UiRun()
    ui.ui_running()
