# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""
import json

import pygame

from settings import Setting


class InfoShow(object):
    def __init__(self, windowSurface, finish):
        # 完成
        self.finish = finish

        self.windowSurface = windowSurface
        self.screen_rect = self.windowSurface.get_rect()

        self.settings = Setting()

        # 实例化一个字体对象
        self.font = pygame.font.Font(self.settings.FONT, 20)
        """
        pygame.font.SysFont系统字体
        pygame.font.Font字体文件
        """

        # 分数字符串
        with open(self.settings.SAVEDATA, "r") as f:
            self.score = json.loads(f.read())

        self.newTime = 0

        # 计分方式
        self.__way = "time"

    @property
    def score_ways(self):
        return self.__way

    @score_ways.setter
    def score_ways(self, way):
        ways = ["time", "click"]
        if way in ways:
            self.__way = way

    def text_display(self, information, pos=None):
        """
        显示文本
        :param information: 信息文本
        :param pos: 显示位置
        :return:
        """

        self.score_image = self.font.render(
            information, True, "red", self.settings.BG_COLOR
        )

        # 设置透明度
        self.score_image.set_alpha(100)
        self.score_rect = self.score_image.get_rect()

        # 右上角
        self.score_rect.right = self.screen_rect.right - 20  # 右边缘与屏幕右边缘相距20像素

        if pos is None:
            self.score_rect.top = 20  # 上边缘与屏幕上边缘也相距20像素
        else:
            self.score_rect.top = pos

        # 在屏幕上显示得分
        self.windowSurface.blit(self.score_image, self.score_rect)

    def info_show(self):
        """
        显示游戏信息
        :return:
        """
        # 难度判断
        self.zh_hard = self.hard_judge()
        # 最高分
        self.oldTime = self.score[self.score_ways][self.hard]

        if not self.finish:
            self.text_display("当前难度：" + str(self.zh_hard))

            if self.score_ways == "time":
                self.text_display("最佳记录：" + str(self.oldTime) + "秒", 60)
                self.text_display("游戏运行：" + str(self.newTime) + "秒", 100)

            if self.score_ways == "click":
                self.text_display("最佳记录：" + str(self.oldTime) + "次", 60)
                self.text_display("点击次数：" + str(self.settings.CLICKNUM) + "次", 100)

        else:  # 输出游戏胜利信息

            self.settings.PAUSE_GAME = False  # 计时停止
            self.text_display("游戏胜利！")

            if self.score_ways == "time":
                self.text_display("当前成绩：" + str(self.newTime) + "秒", 60)
                if self.newTime < self.oldTime:  # 看看是否更新最短时间记录
                    self.save_high_score()

            if self.score_ways == "click":
                self.text_display("当前成绩：" + str(self.settings.CLICKNUM) + "次", 60)
                if self.newTime < self.settings.CLICKNUM:
                    self.save_high_score()

    def save_high_score(self):
        """
        记录最高分
        :return:
        """
        self.score[self.score_ways][self.hard] = self.newTime
        with open(self.settings.SAVEDATA, "w") as f:
            f.write(json.dumps(self.score))

    def hard_judge(self):
        """
        判断难度
        :return:
        """
        if self.settings.VHNUMS <= 3:
            self.hard = "simple"
            return "简单"
        elif self.settings.VHNUMS == 4:
            self.hard = "normal"
            return "普通"
        elif self.settings.VHNUMS >= 5:
            self.hard = "hard"
            return "困难"
