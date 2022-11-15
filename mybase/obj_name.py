# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     :  obj_name.py
# @Time    : 2022/9/2 08-08-50
# @Author  : 穹的兔兔
# @Version : python3.6
# @IDE     : pydrand3
# @Description: 得到实例对象的名字

import traceback


class ObjName(object):
    """
    获取创立的实例对象的名字
    """

    def __init__(self):
        # # 最少只需-1，每导入一次文件-1
        # self.num -= 7
        # (filename, line_number, function_name, text) = traceback.extract_stack()[
        # -self.num
        # ]
        # self.name = text[: text.find("=")].strip()
        pass

    def say_Myname(self):
        (filename, line_number, function_name, text) = traceback.extract_stack()[-3]
        self.name = text[: text.find("=")].strip()
        # print (self.name)
        return self.name


if __name__ == "__main__":
    b = ObjName()
    b.say_Myname()
    a = ObjName()
    a.say_Myname()

"""    
traceback.extract_stack(f=None, limit=None)   

当前堆栈帧中提取原始回溯。返回值的格式与 extract_tb（） 的格式相同。可选的 f 和limit参数与 print_stack（） 具有相同的含义

    返回一个 StackSummary 对象，该对象表示从回溯对象 tb 中提取的“预处理”堆栈跟踪条目的列表。对于堆栈跟踪的备用格式设置非常有用。“预处理”堆栈跟踪条目是一个 FrameSummary 对象，其中包含属性文件名、行号、名称和行，表示通常为堆栈跟踪打印的信息。该行是一个字符串，前导和尾随空格被剥离;如果源不可用，则为“无”。
    
如果limit为正，则最多打印limit条堆栈跟踪条目（从调用点开始）。否则，请打印最后的 abs（limit） 条目。如果省略限制或无，则打印所有条目。可选的 f 参数可用于指定要启动的备用堆栈帧。可选file参数的含义与 print_tb（） 的含义相同

如果 file 被省略或为 None 那么就会输出至标准输出``sys.stderr``，否则它应该是一个打开的文件或者文件类对象来接收输出

打印limit条堆栈跟踪条目，输出至标准输出

print(traceback.extract_stack())
print(traceback.extract_stack()[-2])
print(list(traceback.extract_stack()[-2]))
print(filename,line_number,function_name,text)

堆栈跟踪条目
StackSummary[FrameSummary,...]
[<FrameSummary file /storage/emulated/0/qpython/工程/游戏开发/拼图游戏2/mybase/obj_name.py, line 36 in <module>>, <FrameSummary file /storage/emulated/0/qpython/工程/游戏开发/拼图游 戏2/mybase/obj_name.py, line 20 in __init__>]

<FrameSummary file /storage/emulated/0/qpython/工程/游戏开发/拼图游戏2/mybase/obj_name.py, line 36 in <module>>

FrameSummary,[filename,line_number,function_name,obj_text]
['/storage/emulated/0/qpython/工程/游戏开发/拼图游戏2/mybase/obj_name.py', 36, '<module>', 'b = ObjName()']


print(text.find('=')) #找到=所在位置
print(text[:text.find('=')])#取=前的部分
print(text[:text.find('=')].strip())#去掉所有空格

"""
