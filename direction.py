# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程
# @File    : direction.py
# @Time    : 2022/10/16 11:50
# @Author  : paopaokele
# @Version : python3.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$

from typing import List


class Direction:
    """拼图的now_index,next_index的合法性判断"""

    def __init__(self, rows: int, columns: int):
        """
        该函数获取网格的行数和列数，然后创建一个方向字典，以及两个不能向左或向右移动的位置列表

        :param rows: 网格中的行数
        :type rows: int
        :param columns: 网格中的列数
        :type columns: int
        """

        # 只需初始化类变量。
        self.rows = rows
        self.columns = columns
        self.total = self.rows * self.columns
        # print(self.rows, self.columns)

        self.directions = {
            "up": lambda x: x - self.columns,  # up
            "left": lambda x: x - 1,  # left
            "right": lambda x: x + 1,  # right
            "down": lambda x: x + self.columns,  # down
        }

        # 不能向左，向右的位置
        self.not_left = [self.columns * i for i in range(1, self.columns)]
        self.not_right = list(map(lambda x: x - 1, self.not_left))
        # print(self.not_left, self.not_right)

    def getDirection(self, now_index: int) -> List[int]:
        """
        它返回机器人可以从当前位置移动到的所有可能位置的列表

        :param now_index: 当前位置
        :type now_index: int
        :return: 机器人可以移动到的可能位置列表。
        :rtype: List[int]
        """
        might_pos = []
        for direct in self.directions:  # 方向
            # 向四个方向移动
            next_index = self.directions[direct](now_index)

            if 0 <= next_index < self.total:  # 越界判断
                if now_index in self.not_left and direct == "left":
                    ...
                elif now_index in self.not_right and direct == "right":
                    ...
                else:
                    might_pos.append(next_index)
        return might_pos

    def isValiad(self, now_index: int, next_index: int) -> bool:
        """

        :param now_index: 节点的当前索引
        :param next_index: 当前索引的下一个索引
        :return: 有效是否
        """
        valiad = self.getDirection(now_index)
        if next_index in valiad:
            return True
        return False


if __name__ == "__main__":
    grid = [
        ["1", "0", "0", "0"],
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"],
    ]

    grid = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # 5,4
    # 4,9,14--5n-1
    # 5,10,15----5n----1<=n<=4-1----not left

    s = Direction(4, 5)
    res = s.getDirection(14)
    print(res)
    print(s.isValiad(4, 3))
