#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/21 17:57
# @File: dazyimport.py
# @Software: Program
# @Desc: dazyimport


class LazyImport(object):
    """动态导入"""

    def __init__(self, module_name: str, module_class: str):
        self.module_name = module_name
        self.module_class = module_class
        self.module = None

    def __getattr__(self, name: str) -> object:
        if self.module is None:
            self.module = __import__(self.module_name, fromlist=[self.module_class])
        return getattr(self.module, name)
