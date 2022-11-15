# -*- coding: UTF-8 -*-
"""
@summary:https://blog.csdn.net/kobeyu652453/article/details/108732747
@usage:
"""

import os
import sys


# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, "frozen", False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_cmd(ico, main, *args):
    """
    获取打包文件的命令
    :param main:
    :param args:
    :return:
    """
    a = "pyinstaller " + "-w " + "-i " + ico + " " + main + " "

    b = ""
    c = ""
    for item in args:
        be = "-p" + " " + item + " "
        b += be
        # print('a.py'.split('.')[0])
        ce = "--hidden-import" + " " + item.split(".")[0] + " "
        c += ce

    d = a + b + c
    return d


def cmd_get_auto(ico, main, dict):
    """

    :param ico: 图标
    :param main: 主模块
    :param dict: 文件路径
    :return:
    """
    a = "pyinstaller " + "-w " + "-i " + ico + " " + main + " "

    abs_path = os.listdir(dict)
    abs_path.remove(ico)
    abs_path.remove(main)
    abs_path.remove("__pycache__")

    b = ""
    c = ""
    for item in abs_path:
        be = "-p" + " " + item + " "
        b += be

        ce = "--hidden-import" + " " + item.split(".")[0] + " "
        c += ce

    d = a + b + c
    return d


"""
打包方法：
1，在Explorer中显示，路径行   cmd

2,打包exe
cmd_get_auto()得到命令行，输入
pyinstaller -w -i loli.jpg main.py -p button.py -p event.py -p move.py -p resource -p settings.py -p text_info.py -p 拼图游戏2.py -p MyThread.py --hidden-import button --hidden-import event --hidden-import move --hidden-import resource --hidden-import settings --hidden-import text_info --hidden-import 拼图游戏2 --hidden-import 测试1
-w：不显示控制台，-i:图标

3，打包资源
删除build,dist文件夹.修改spec
datas=[('resource','resource')]

再次打包exe，只打包main.spec
pyinstaller  main.spec
报错去掉-F

4，dist文件夹中找到exe文件

5，减少exe文件包大小的方法
exe文件所在文件夹，按大小排序，从大到小删除文件与文件夹，到exe文件不能运行为止
资源中音乐文件较大
"""
if __name__ == "__main__":
    # 访问res文件夹下数据.txt的内容
    # filename = resource_path(os.abstruct_path.join("素材", "外星人", '亚丝娜.png'))
    # print(filename)
    # print(os.abstruct_path.join("素材", "外星人", '亚丝娜.png'))

    # e = get_cmd('loli.jpg', 'main.py', )
    # print(e)

    # b = os.listdir('../拼图游戏2')
    # print(b)

    c = cmd_get_auto("loli.jpg", "main.py", "../拼图游戏2")
    print(c)
