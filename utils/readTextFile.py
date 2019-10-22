#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/22 15:47
# @File: readTextFile.py
# @Software: Program
# @Desc: read display text file
from typing import TextIO


def read_file(fname: str) -> None:
    """ read file """
    fobj: TextIO
    try:
        fobj = open(fname, mode='r', encoding='utf-8')
    except IOError as e:
        print("*** file open error:", e)
    finally:
        for line in fobj:
            print(line)
        fobj.close()

