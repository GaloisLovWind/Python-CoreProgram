#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-19
    Desc:Decorator function
"""
from time import ctime,sleep

def tsfunc(func):
    def wrapperFunc():
        print("[%s] %s() called"%(ctime(),func.__name__))
        return func()
    return wrapperFunc

@tsfunc
def foo():
    pass

def test1():
    foo()
    sleep(4)
    for i in range(2):
        sleep(1)
        foo()
def convert(func,seq):
    """conv,sequenue of numbers to same type"""
    return [func(eachNum) for eachNum in seq]
def test2():
    """调用函数"""
    myseq = (123,45.67,-6.2e8,999999999)
    print(convert(int,myseq))
    print(convert(float,myseq))

