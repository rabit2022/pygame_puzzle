import datetime

import pygame
from pygame.locals import *

from color import Color
from info import InfoShow
from main_event import MainEvent
from move import Move
from settings import Setting
from ui_main import UiRun


class Game(object):
    def __init__(self):
        pygame.init()

        # 计时器
        self.mainClock = pygame.time.Clock()

        self.settings = Setting()
        self.move = Move()

        self.ui = UiRun()
        self.ui.ui_running()

        # 图片
        self.gameImage = self.ui.gameImage
        self.gameRect = self.gameImage.get_rect()

        # 设置窗口，窗口的宽度和高度取决于图片的宽高
        self.windowSurface = pygame.display.set_mode(
            (self.gameRect.width, self.gameRect.height)
        )

        # 标题
        pygame.display.set_caption("小小拼图")
        # 设置小图标，当前图片
        pygame.display.set_icon(self.gameImage)

        # UI加载完毕计时
        self.start = datetime.datetime.now()

        # 每小块，白块
        self.gameBoard, self.blackCell = self.move.newGameBoard()

        # 绘制cell
        self.cellWidth = int(self.gameRect.width / self.settings.VHNUMS)
        self.cellHeight = int(self.gameRect.height / self.settings.VHNUMS)

        self.event_main = MainEvent(self)

        # 完成与否
        self.finish = False
        # 右上角提示文字
        self.text = InfoShow(self.windowSurface, self.finish)

        # 计分方式
        if self.ui.isButton(3):
            self.text.score_ways = "time"
        if self.ui.isButton(4):
            self.text.score_ways = "click"

        self.music_path = self.ui.music_path
        # 音乐播放
        # self.settings.music(self.music_path)

    def game_running(self):
        # 游戏主循环
        while True:
            # 键盘事件检测
            self.event_main.check_events()

            if self.settings.PAUSE_GAME:  # 暂停
                # 计时器
                self.end = datetime.datetime.now()
                self.text.newTime = (self.end - self.start).seconds

                # 更新finish值
                self.text.finish = self.finish

                if self.move.isFinished():
                    # 是否完成,完成后按顺序填充每张图片
                    self.gameBoard = self.move.get_full_picture()
                    # 下面的不够稳定, 常报错
                    # self.gameBoard[self.blackCell] = self.settings.CELLNUMS - 1
                    self.finish = True

                self.windowSurface.fill(self.settings.BG_COLOR)

                # 绘制每一张图片，线条，游戏信息
                self.draw_slice()

                # 完成后不再划线
                if not self.finish:
                    self.draw_lines()
                else:
                    ...

                self.text.info_show()

                pygame.display.update()
                self.mainClock.tick(self.settings.FPS)

    def draw_slice(self):
        """
        # 绘制每一张图片
        :return:
        """
        for i in range(self.settings.CELLNUMS):
            # 生成每个位置的矩形(0,0),(0,1),(0,2)
            rowDst = int(i / self.settings.VHNUMS)
            colDst = int(i % self.settings.VHNUMS)
            rectDst = pygame.Rect(
                colDst * self.cellWidth,
                rowDst * self.cellHeight,
                self.cellWidth,
                self.cellHeight,
            )

            if self.gameBoard[i] == -1:
                # 标记为-1时,跳过绘制图片，显示空白
                continue

            rowArea = int(self.gameBoard[i] / self.settings.VHNUMS)
            colArea = int(self.gameBoard[i] % self.settings.VHNUMS)
            rectArea = pygame.Rect(
                colArea * self.cellWidth,
                rowArea * self.cellHeight,
                self.cellWidth,
                self.cellHeight,
            )

            self.windowSurface.blit(self.gameImage, rectDst, rectArea)

            """
            blit（source, dest, area=None, special_flags = 0）,返回值为rect对象，返回被改变的画面区域。
            source：一个surface对象，可以理解为一张图；
            dest：一个可以标识坐标的东西，可以是一个（x，y）元组。也可以是一个（x，y，height，width）元组，也可以是一个Rect对象，Rect对象可以理解为有位置有大小的矩形。
            area：一个Rect对象
            其中，source就是你要复制粘贴到B上的A图片。
            """

    def draw_lines(self):
        """
        绘制线条
        :return:
        """
        for i in range(self.settings.VHNUMS + 1):
            pygame.draw.line(
                self.windowSurface,
                Color.black.value,
                (i * self.cellWidth, 0),
                (i * self.cellWidth, self.gameRect.height),
            )

        for i in range(self.settings.VHNUMS + 1):
            pygame.draw.line(
                self.windowSurface,
                Color.black.value,
                (0, i * self.cellHeight),
                (self.gameRect.width, i * self.cellHeight),
            )

    def universal_events(self, event):
        """
        其他通用按键
        :param event:
        :return:
        """
        if event.key == K_c:
            # 重新开始游戏
            game = Game()
            game.game_running()
        if event.key == pygame.K_z:
            # 更换音乐
            self.settings.music()


if __name__ == "__main__":
    game = Game()
    game.game_running()
