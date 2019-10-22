#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/22 23:36
# @File: question.py
# @Software: Program
# @Desc: 编写的代码只是其中的部分，有些过于重复和简单，没有编写执行
"""
    cmd: python app.py --file_name=5_number
    enter keyboard : 1
"""
import operator

def test1() -> None:
    """ Number Type """
    aInt: int = 1
    aFloat: float = 3.5
    aBool: bool = False
    aComplex: complex = 1 + 1j
    print("aInt = ", aInt)
    print("aFloat = ", aFloat)
    print("aBool = ", aBool)
    print("aComplex = ", aComplex)


def test2() -> None:
    """ operator """
    print("1.1 + (1 + 1.1j) = ", 1.1 + (1 + 1.1j))
    print("1.1 + 1 = ", 1.1 + 1)
    print("1 + True = ", 1 + True)
    print("-" * 20, " calculate operator")
    print("2 * 3 = ", 2 * 3)
    print("2 / 3 = ", 2 / 3)
    print("2 // 3 = ", 2 // 3)
    print("2 ** 3 = ", 2 ** 3)
    print("2 % 3 = ", 2 % 3)
    print("-" * 20, " bit operator")
    print("2 >> 3 = ", 2 >> 3)
    print("2 << 3 = ", 2 << 3)
    print("2 ^ 3 = ", 2 ^ 3)
    print("2 & 3 = ", 2 & 3)
    print("2 | 3 = ", 2 | 3)
    print("~2 = ", ~2)


def test3() -> None:
    """ build-in function python3 不存在 cmp 方法，使用的是 operator 模块的中方法"""
    print("operator.gt(-6 ,2) =", operator.gt(-6, 2))
    print("operator.gt(-6 ,2) =", operator.gt(0xFF, 255))
    print("str(0xFF) = ", str(0xFF))
    print("type(0xFF) = ", type(0xFF))
    print("type(1 + 1j) = ", type(1 + 1j))
    print("-" * 20)
    print("int(1.1) = ", int(1.1))
    print("complex(2, 4) = ", complex(2, 4))
    print("float(4) = ", float(4))


def test4() -> None:
    """ Special build-in function """
    c: C = C()
    print("bool(c) = ", bool(c))  # Python3 不支持 __nonzero__ 改成 __bool__


class C(object):

    def __nonzero__(self) -> None:
        return False

    def __bool__(self):
        return True
    # def __len__(self):
    #     return 1