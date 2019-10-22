#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/22 15:32
# @File: makeTextFile.py
# @Software: Program
# @Desc: create text file
from typing import List, TextIO
import os


def exist_file(fname: str) -> bool:
    """ check file """
    if os.path.exists(fname):
        print("'%s' exists" % fname)
        return True
    return False


def enter_save() -> List[str]:
    """save data which user enter the content"""
    all: List[str] = []
    print("\n Enter lines ('.' by itself to quit).\n")
    while True:  # loop until user terminates input
        entry: str = input(">")
        if entry == ".":
            break
        else:
            all.append(entry)
    return all


def get_filename(rootdir:str) -> str:
    """ get filename """
    while True:
        fname = input("Enter filename:")
        fpath = os.path.join(rootdir, fname)
        if os.path.exists(fpath):
            return fpath
        print("Error: '%s' does not exist" % fpath)


def write_data_to_file(fname: str = 'data.txt') -> None:
    """ write data what user enter to file """
    # fname: str = "data.txt"
    ls: str = os.linesep
    is_exist: bool = exist_file(fname)
    if is_exist:
        all: List[str] = enter_save()
        fobj: TextIO = open(fname, 'w')
        fobj.writelines(['%s%s' % (x, ls) for x in all])
        fobj.close()
        print("Done")
    else:
        print("Error: '%s' does not exist" % fname)
