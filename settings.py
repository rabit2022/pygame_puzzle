# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""
import os
import random

import pygame

from color import Color
from mybase import Variable, Singleton


class Setting(Singleton):
    # 一些常量
    WIDTH = 500
    HEIGHT = 500
    FPS = 40
    BG_COLOR = Color.light_gray.value  # (255, 255, 255)

    # 3*3分割
    VHNUMS = Variable(3)
    CELLNUMS = Variable("VHNUMS * VHNUMS")  # 单元格数量

    def __init__(self):
        self.MAXRANDTIME = 1000  # 随机移动次数

        self.CLICKNUM = 0
        self.PAUSE_GAME = True

        # https://www.aigei.com/font/class/lovely_5-style_between_the_ru/?detailTab=file
        self.FONT = "./resource/font/小南同学.ttf"
        self.SAVEDATA = "./resource/saveData/rank.json"
        self.IMAGE = "./resource/images/"
        self.MUSIC = "./resource/music/"

    def music(self, music_path=None):
        """
        添加背景音乐
        :return:
        """
        """
        音乐格式转换在线
        https://convertio.co/zh/audio-converter/
        """

        if music_path is None:
            music_dir = self.MUSIC
            music_path = music_dir + random.choice(os.listdir(music_dir))

        print(music_path)

        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)  # 循环次数  -1表示无限循环


if __name__ == "__main__":
    a = Setting()
    print(a.VHNUMS)
    print(a.CELLNUMS)
    a.VHNUMS = 5
    print(a.VHNUMS)
    print(a.CELLNUMS)
