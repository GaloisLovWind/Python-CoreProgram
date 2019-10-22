#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-15
    Desc:Functional programming
"""

def hello():
    print("hello world")
def foo():
    return ['xyz',100000,-98.6]
def bar():
    return ('abc',[43,'python'],'Guido')
def test1():
    """返回值与函数类型"""
    res = hello()
    print(res)
    print(type(res))
    print("---------------------")
    aTuple = bar()
    x,y,z = bar()
    print(aTuple)
    print(x,y,z)
