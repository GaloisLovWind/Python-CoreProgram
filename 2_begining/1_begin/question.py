#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/21 19:23
# @File: question.py
# @Software: Program
# @Desc: input()
"""
    cmd: python app.py --file_name=2_begining
    enter keyboard : 1
"""
from decimal import Decimal
from typing import List, Tuple, Dict, TextIO, TypeVar
import os

StrAndInt = TypeVar('StrAndInt', str, int, Tuple, List, Dict)


def test1() -> None:
    """  print() 方法调用 """
    my_string: str = "Hello World"
    print(my_string)
    print("%s is number %d" % ("Python", 1))


def test2() -> None:
    """ input 方法调用 """
    user: str = input("Enter Login Name:")
    print("You login is: ", user)
    num: str = input("Now enter a number:")
    print("Doubling your number: ", int(num) * 2)


def test3() -> None:
    """ 运算符 """
    print("-2 * 4 + 3 ** 2 = ", -2 * 4 + 3 ** 2)
    print("4 // 3 = ", 4 // 3)


def test4() -> None:
    """ 数字 Dcimal"""
    print(1.10000000000000000000000000000001)
    print("Decimal(1.1) = ", Decimal(1.10000000000000000000000000000001))


def test4() -> None:
    """ 字符串 """
    py_str: str = "Python"
    is_cool: str = "is cool"
    print("py_str = ", py_str)
    print("is_cool = ", is_cool)
    print("py_str[0] = ", py_str[0])
    print("py_str[-1] = ", py_str[-1])
    print("py_str[2:5] = ", py_str[2:5])
    print("is_cool[:2] = ", py_str[:2])
    print("py_str + is_cool = ", py_str + is_cool)
    print("py_str * 2 = ", py_str * 2)


def test5() -> None:
    """ 元组 """
    aList: List[int] = [1, 2, 3, 4]
    print("aList = ", aList)
    print("aList[0] = ", aList[0])
    print("aList[2:] = ", aList[2:])
    print("aList[:3] = ", aList[:3])
    aList[1] = 5
    print("aList[1] = 5; aList = ", aList)
    aTuple: Tuple[str, int, int, str] = ("Galois", 77, 93, "Gauss")
    print("aTuple = ", aTuple)
    print("aTuple[:3] = ", aTuple[:3])
    aTuple[1] = 5


def test6() -> None:
    """ Dict """
    aDict: Dict[str, int] = {'host': 'earth'}
    print("aDict = ", aDict)
    aDict['port'] = 80
    print("aDict['port'] = 80; aDict = ", aDict)
    print("aDict.keys() = ", aDict.keys())
    print("aDict['host'] = ", aDict['host'])
    print("aDict.values() = ", aDict.values())
    for key in aDict:
        print("for-in: key, value --", key, aDict[key])


def test7() -> None:
    """ for-in, range() """
    print(" for-in [0, 1, 2]")
    for eachNum in [0, 1, 2]:
        print(eachNum)
    print(" range(3) ")
    for eachNum in range(3):
        print(eachNum)
    foo: str = "abc"
    print("for-in foo = ", foo)
    for c in foo:
        print(c)
    for i in range(len(foo)):
        print(foo[i], " -- [%d]" % i)
    print("enumerate(foo)")
    for i, ch in enumerate(foo):
        print(ch, " -- (%d)" % i)


def test8() -> None:
    """ 列表解析 """
    squard: List[int] = [x ** 2 for x in range(4)]
    print(" for-in squard = [x ** 2 for x in range(4)] :", squard)
    for i in squard:
        print(i)
    sqdEvents = [x ** 2 for x in range(8) if not x % 2 == 0]
    print(" for-in sqdEvents = [x ** 2 for x in range(8) if not x % 2 == 0] :", sqdEvents)
    for i in sqdEvents:
        print(i)


def test9() -> None:
    """ open() """
    fobj: TextIO = open(os.path.join(os.path.dirname(__file__), 'menu.txt'), mode='r', encoding='utf-8')
    for line in fobj:
        print(line)
    fobj.close()


def test10() -> None:
    """ try-except 错误和异常 """
    filename = input("Enter file name in the current path: ")
    try:
        fobj: TextIO = open(os.path.join(os.path.dirname(__file__), filename), mode='r', encoding='utf-8')
        for line in fobj:
            print(line)
        fobj.close()
    except IOError as e:
        print("file open error:", e)
    finally:
        print("end")


def test11() -> None:
    """ function """
    print("use addMe2Me(2) :", addMe2Me(2))
    print("use addMe2Me('Python') :", addMe2Me('Python'))
    print("use addMe2Me([-1, 'Python']) :", addMe2Me([-1, 'Python']))
    print("function with default argument : ")
    print("use foo(): ", foo())
    print("use foo(False): ", foo(False))


def test12():
    """ Class 类"""
    foo1: FooClass = FooClass()
    print("foo: FooClass = FooClass()")
    print("use foo.showname() ", foo1.showname())
    print("use foo.showversion() ", foo1.showversion())
    foo2: FooClass = FooClass('Abel')
    print("foo2: FooClass = FooClass('Abel')")
    print("use foo.showname() ", foo2.showname())
    print("use foo.showversion() ", foo2.showversion())

    FooClass.version = 1.0
    print("FooClass.version = 1.0")
    print("use foo.showversion() ", foo1.showversion())
    print("use foo.showversion() ", foo2.showversion())

    foo1.version = 2.0
    print("FooClass.version = 2.0")
    print("use foo.showversion() ", foo1.showversion())
    print("use foo.showversion() ", foo2.showversion())


def addMe2Me(x: StrAndInt) -> StrAndInt:
    """ apply + opration to argument"""
    return x + x


def foo(debug: bool = True) -> None:
    """ determin if in debug mode with default argument """
    if debug:
        print("in debug mode")
    print("done")


class FooClass(object):
    """ my very first class: FooClass"""
    version: int = 0.1

    def __init__(self, nm: str = "Galois") -> None:
        """ constructor"""
        self.name = nm
        print("Create a Instance for ", nm)

    def showname(self) -> None:
        """ display instance attribute  and class name"""
        print("Your name is ", self.name)
        print("My name is ", self.__class__.__name__)

    def showversion(self) -> None:
        """ display class(static) attribute """
        print(self.version)