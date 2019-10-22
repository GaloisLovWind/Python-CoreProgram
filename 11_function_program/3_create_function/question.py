#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-15
    Desc:Create function
"""
def helloSomeone(who):
    """
    :param who:
    :return:a salutory string customized with input
    """
    return "Hello "+str(who)
def test1():
    """def 语句"""
    who = input("What is your name?")
    ans = helloSomeone(who)
    print(ans)
def foo():
    def bar():
        print("bar() called")
    print("foo() called")
    bar()
def test2():
    """内嵌函数"""
    foo()
    # bar()
