# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     :  sigle.py
# @Time    : 2022/9/2 12-02-36
# @Author  : 穹的兔兔
# @Version : python3.6.4
# @IDE     : pydrand3
# @Description: 单例模式
# @origion:https://www.zhihu.com/tardis/sogou/art/87524388


"""
一，单例模式
一种软件设计模式，而不是专属于某种编程语言的语法；
单例模式只有一个实例存在；
单例模式有助于协调系统的整体性、统一性；

二，软件设计模式
工厂模式
原型模式
单例模式
生成器模式
......
使用合理的软件设计模式可以使得代码重用性更高、更易于理解、可靠性更高。
"""


# 三，实理方法
# 1，对new方法进行重写，


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


"""        
#凡是继承Singleton基类的子类都属于单例模式
#id却是相同的，也就说这两个实例指向同一个地址，为同一个实例

class Books(Singleton):
    def __init__(self):
        pass

book1 = Books()
book2 = Books()
print(id(book1))
print(id(book2)) 
    
    

#2，利用装饰器实现Python单例模式就是通过类进行操作实现单例模式，
"""


def singleton(cls, ):
    instances = {}

    def wrapper(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        # print("单例")
        return instances[cls]

    return wrapper


class SingletonClass(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kw):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls(*args, **kw)
        return self._instance[self._cls]


"""
#然后调用装饰器，实现单例模式，
@singleton
class Animal(object):
    def __init__(self):
        pass
    
animal1 = Animal()
animal2 = Animal()
print(id(animal1))
print(id(animal2))

3，其他方法
__metaclass__元类、共有属性等来实现，但是由于它本质上与上述两种方式并没有什么区别，也许看代码过程中会觉得有点不太明白，其实上述两种方式都是基于同一个思想进行实现的：创建实例(instance)时首先判断是否已经存在，如果已经存在则返回，否则创建。
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# @SingletonClass
# class MySQL(metaclass = SingletonMeta):
# class MySQL(object):
class MySQL(Singleton):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


"""
4，使用场景
资源管理的场景
难以同步的场景
涉及共享的场景
有关认证的场景
"""

import threading


# 多线程
class Singleton(object):
    """
    实例化一个对象
    """

    # 锁
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


if __name__ == "__main__":
    a = MySQL("aa", "aaa")
    b = MySQL("bb", "bbb")
    print(a.ip)
    a.ip = "cc"
    print(b.ip)

    print(id(a) == id(b))
