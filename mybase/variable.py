# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     :  mybase.py
# @Time    : 2022/9/1 22-29-30
# @Author  : 穹的兔兔
# @Version : python3.6.4
# @IDE     : pydrand3
# @Description: 描述符

from .obj_name import ObjName


# from obj_name import ObjName


class Meta(type):
    """
    元类，把val属于Field2的key，转为私有化属性
    """

    def __new__(meta, name, bases, class_dict):
        # print(meta, name, bases, class_dict)
        for key, val in class_dict.items():
            # if isinstance(val, Variable):
            if hasattr(val, memory):
                class_dict.update(val.memory)
        return type.__new__(meta, name, bases, class_dict)


class Variable(ObjName):
    # 实现函数关系，改变一个变量值，其他变量也会动
    memory = {}
    key = None

    def __init__(self, num, initial=0):
        super().__init__()
        self.key = self.say_Myname()
        self.initial = initial

        if isinstance(num, Variable):
            self.num = num.num
        else:  # str与num均直接赋值
            self.num = num

        self.update_memory(self.num)

    def update_memory(self, value):
        # 每次更新时，key:value加入memory中
        self.value = value
        self.memory[self.key] = value
        # print(self.memory)

    def process_str(self, info):
        # 处理字符串
        operations = info.split()
        result = ""
        for operate in operations:
            try:
                # 在memory中取值
                operate = self.memory[operate]
            except KeyError as k:
                # 没有变量时自行添加，防止未定义的错误
                # 存储时用str以便于get，当下则用str,以组合编译
                # 未定义用初始化解决，有时初始值未必符合要求
                """
                self.memory[operate] = 0
                operate = "0"
                """
                if operate not in "+-*/=<>([{}]) ":
                    self.memory[operate] = self.initial
                    operate = str(self.initial)
            else:
                # memory中value有num类型
                operate = str(operate)
            finally:
                result += operate
        # print(result)
        return result

    def __get__(self, instance, instance_type):
        # self.instance = instance
        # self.instance_type = instance_type

        if instance is None:
            return self
        elif isinstance(self.num, str):
            # print(self.num)
            # 处理字符串
            aa = self.process_str(self.num)
            """
            bb=0
            dictA = {}# 创建接收dict对象
            exec("bb="+aa,locals(),dictA)
            # globals参数传入局部变量locals()，locals参数传入dictA
            bb = dictA['bb']# 自dictA中取出bb 
            """
            # 计算表达式
            bb = eval(aa)
            return bb
        else:
            return self.num

    def __set__(self, instance, value):
        self.num = value
        # 维护memory
        self.update_memory(self.num)

    def __mul__(self, other):
        num = self.__get__("", "")
        # *定义
        if isinstance(other, Variable):
            other = other.__get__("", "")
            return Variable(num * other)
        elif isinstance(other, (int, float)):
            return Variable(num * other)

    def __sub__(self, other):
        num = self.__get__("", "")
        if isinstance(other, Variable):
            other = other.__get__("", "")
            return Variable(num - other)
        elif isinstance(other, (int, float)):
            return Variable(num - other)


class Setting(object):
    CELLNUMS = Variable("VHNUMS * VHNUMS")  # 单元格数量
    # 3*3分割
    VHNUMS = Variable(3)


def p():
    print(b.VHNUMS)
    print(b.CELLNUMS)
    print("*" * 30)


if __name__ == "__main__":
    b = Setting()
    p()

    b.VHNUMS = 6
    p()

    b.CELLNUMS = 2
    p()

    b.VHNUMS = 3
    p()

    b.CELLNUMS = "VHNUMS ** 2"
    p()
