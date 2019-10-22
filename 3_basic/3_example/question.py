#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/22 15:32
# @File: question.py
# @Software: Program
# @Desc: question
"""
    cmd: python app.py --file_name=3_basic
    enter keyboard : 3
"""
import os

from utils.makeTextFile import get_filename, write_data_to_file
from utils.readTextFile import read_file


def test1():
    """ a example for write file and read file"""
    rootdir: str = os.path.dirname(__file__)
    fpath: str = get_filename(rootdir)
    write_data_to_file(fpath)
    read_file(fpath)