#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-26
    Desc:Recursion
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def test1():
    print(factorial(5))