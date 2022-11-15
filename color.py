# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     :  colors.py
# @Time    : 2022/9/1 21-53-55
# @Author  : 穹的兔兔
# @Version : python3.6.4
# @IDE     : pydrand3
# @Description: 颜色的枚举

from enum import Enum


class Color(Enum):
    # 兼容
    # Define colors（红，绿，蓝）255
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    light_gray = (230, 230, 230)

    ## 定义颜色
    # 红色系
    RED = (255, 0, 0)
    DARKRED = (139, 0, 0)
    # 橙色系
    GOLD = (255, 215, 0)
    ORANGE = (255, 165, 0)
    DARKORANGE = (255, 140, 0)
    # 黄色系
    LIGHTYELLOW = (255, 255, 224)
    YELLOW = (255, 255, 0)
    # 绿色系
    LIMEGREEN = (50, 205, 50)
    GREEN = (0, 255, 0)
    SPRINGGREEN = (0, 255, 127)
    SEAGREEN = (46, 139, 87)
    OLIVE = (128, 128, 0)
    # 青色系
    CYAN = (0, 255, 255)
    DARKCYAN = (0, 139, 139)
    # 蓝色系
    LIGHTSKYBLUE = (135, 206, 250)
    SKYBLUE = (135, 206, 235)
    DEEPSKYBLUE = (0, 191, 255)
    LIGHTSTEELBLUE = (176, 196, 222)
    BLUE = (0, 0, 255)
    MEDIUMBLUE = (0, 0, 205)
    DARKBLUE = (0, 0, 139)
    # 紫色系
    VIOLET = (238, 130, 238)
    FUCHSIA = (255, 0, 255)
    PURPLE = (128, 0, 128)
    INDIGO = (75, 0, 130)
    # 粉色系
    PINK = (255, 192, 203)
    LIGHTPINK = (255, 182, 193)
    DEEPPINK = (255, 20, 147)
    # 白色系
    WHITE = (255, 255, 255)
    SNOW = (255, 250, 250)
    AZURE = (240, 255, 255)
    # 灰色系
    LIGHTGRAY = (211, 211, 211)
    SILVER = (192, 192, 192)
    DARKGRAY = (169, 169, 169)
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)
    # 棕色系
    WHEAT = (245, 222, 179)
    CHOCOLATE = (210, 105, 30)
    BROWN = (165, 42, 42)


# 常用颜色
white = Color.white.value
black = Color.black.value
red = Color.red.value
green = Color.green.value
blue = Color.blue.value

light_gray = Color.light_gray.value

if __name__ == "__main__":
    print(Color.red.value)
