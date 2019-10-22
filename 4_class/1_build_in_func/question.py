#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/22 19:39
# @File: question.py
# @Software: Program
# @Desc: question
"""
    cmd: python app.py --file_name=4_class
    enter keyboard : 1
"""
from typing import TypeVar

Number = TypeVar('Number', int, float, complex, str)


def displayNumberType(num: Number) -> None:
    """ type() """
    print(num, "is", end=" ")
    if type(num) == type(0):
        print("an integer")
    elif type(num) == type(0.0):
        print("an float")
    elif type(num) == type(0 + 0j):
        print("an complex")
    else:
        print("not a number at all")


def displayNumberType2(num: Number) -> None:
    """ type() """
    print(num, "is", end=" ")
    if type(num) == int:
        print("an integer")
    elif type(num) == float:
        print("an float")
    elif type(num) == complex:
        print("an complex")
    else:
        print("not a number at all")


def displayNumberType3(num: Number) -> None:
    """ type() """
    print(num, "is", end=" ")
    if isinstance(num, int):
        print("an integer")
    elif isinstance(num, float):
        print("an float")
    elif isinstance(num, complex):
        print("an complex")
    else:
        print("not a number at all")


def test1() -> None:
    """ build-in function """
    print("-" * 20, " type()")
    displayNumberType(1)
    displayNumberType(2.2)
    displayNumberType(1 + 1j)
    displayNumberType("a")
    print("-" * 20, " types module")
    displayNumberType2(1)
    displayNumberType2(2.2)
    displayNumberType2(1 + 1j)
    displayNumberType2("a")
    print("-" * 20, " isinstance()")
    displayNumberType3(1)
    displayNumberType3(2.2)
    displayNumberType3(1 + 1j)
    displayNumberType3("a")
