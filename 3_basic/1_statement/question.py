#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/22 1:13
# @File: question.py
# @Software: Program
# @Desc: question

"""
    cmd: python app.py --file_name=3_basic
    enter keyboard : 1
"""
from typing import List, Tuple, Dict, TextIO, TypeVar

StrAndInt = TypeVar('StrAndInt', str, int, Tuple, List, Dict)


def test1():
    """ statement """
    weather_is_hot: int = 1
    show_warning: int = 0
    # check conditions
    if (weather_is_hot == 1) and \
            (show_warning == 0):
        print("Yes")
    print("No")
    import sys; x: str = "foo"; sys.stdout.write(x + "\n")