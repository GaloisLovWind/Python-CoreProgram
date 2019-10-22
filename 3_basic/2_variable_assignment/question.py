#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/22 14:25
# @File: question.py
# @Software: Program
# @Desc: question
"""
    cmd: python app.py --file_name=3_basic
    enter keyboard : 2
"""
from typing import List, Tuple, Dict, TextIO, TypeVar

StrAndInt = TypeVar('StrAndInt', str, int, Tuple, List, Dict)


def test1() -> None:
    """ 赋值运算符 """
    aString: str = "cart"
    aInt: int = -12
    anotherString: str = "shop" + "ing"
    aFloat: float = -3.14 * (5.0 ** 2)
    aList: List[float, str, complex] = [3.14e10, '2nd elmt of list', 8.82 - 4.371j]
    print("aString = ", aString)
    print("aInt = ", aInt)
    print("anotherString = ", anotherString)
    print("aFloat = ", aFloat)
    print("aList = ", aList)


def test2() -> None:
    """ 增量运算符 """
    x: int = 1
    x += 1
    print("x = 1; x += 1; x =", x)
    y: str = 'Python'
    # y += 123 # 不支持 字符串和字符串的 加法运算
    y += " World"
    print("y = 'Python', y += 'World'; y =", y)
    aTuple: Tuple[int, int] = (1, 2)  # 不可变对象
    print("type(aTuple):", id(aTuple))
    aTuple += (3,)
    print("aTuple= (1, 2); aTuple += (3,); aTuple = ", aTuple, id(aTuple))
    aList: List[int] = [1, 2]  # 可变对象
    print("type(aList):", id(aList))
    aList += [3]
    print("aList= [1, 2]; aList += [3]; aList = ", aList, id(aList))


def test3() -> None:
    """ 多重赋值 """
    x = y = z = 1  # type: int
    print("x = y = z = 1; ", x, y, z)


def test4() -> None:
    """ 多元赋值 """
    (x, y, z) = (1, 2, "a string")
    print("x, y, z = 1, 2, 'a string'", x, y, z)
    x, y = 1, 2
    x, y = y, x  # 交换
    print("x, y = 1, 2; x, y = y, x,", x, y)

