#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Galois
# @Date: 2019/10/21 18:18
# @File: excute_package_method.py
# @Software: Program
# @Desc: excute_package_method
import os
import sys
from typing import List, Tuple, Union

from utils.dazyimport import LazyImport


class ExecuteProgramForModule(object):

    def __init__(self, execute_dir: str, file_name: str, module_name: str = "question",
                 menu_file: str = "menu.txt", method_prefix: str = "test") -> None:
        """
            构造方法
        :param execute_dir:  执行的主目录
        :param file_name:  文件目录
        :param module_name: 执行的模块文件名
        :param menu_file: 索引目录
        :param method_prefix: 执行方法前缀
        """
        self.execute_dir = execute_dir
        self.file_name = file_name
        self.module_name = module_name
        self.menu_file = menu_file
        self.method_prefix = method_prefix

    def run(self):
        package_list = self._read_package_list()
        ExecuteProgramForModule.print_package(package_list)
        is_select, index = ExecuteProgramForModule.get_select_index(len(package_list))
        if is_select and index == 0:
            sys.exit(0)
        package_name: str = package_list[index - 1]
        while True:
            method_sum: int = self._read_execute_method_count(package_name)
            is_select, index = ExecuteProgramForModule.get_select_index(method_sum)
            if not is_select:
                continue
            if index == 0:
                break
            print('\033[0m')
            try:
                is_true = self.execute_method(package_name, index)
                if not is_true:
                    print("the module hasn't this method")
            except TypeError as e:
                print("Programming what you execute has error:", e.__traceback__)
            print('\033[31m')
        sys.exit(0)

    def _read_package_list(self) -> List[str]:
        """
            读取文件夹类所有的包名, 且按照 文件名的索引排序
        :return:
        """
        package_path: str = os.path.join(os.path.dirname(self.execute_dir), self.file_name)
        path_dir: List[Union[bytes, str]] = os.listdir(package_path)  # 读取文件夹
        package_list: List[str] = []  # 文件夹类所有的包名
        print("Please select the module what you want to import[e\\q exit]:")
        for directory in path_dir:
            if not os.path.isfile(directory):
                package_list.append(directory)
        package_list = sorted(package_list, key=lambda name: int(str(name).split('_')[0]))
        return package_list

    def _read_execute_method_count(self, package_name: str) -> int:
        """
            获得执行的个数
        :param package_name:
        :return:
        """
        package_file = os.path.join(os.path.dirname(self.execute_dir), self.file_name, package_name)
        menu_file: str = os.path.join(package_file, self.menu_file)
        return ExecuteProgramForModule.read_menu(menu_file)

    def execute_method(self, package_name: str, index: int) -> bool:
        """
            根据索引执行包里的方法
            :param package_name: 包名
            :param index: 索引
            :return:
        """
        modname = "%s.%s.%s" % (self.file_name, package_name, self.module_name)
        method = "%s%d" % (self.method_prefix, index)
        importable = LazyImport(modname, method)
        is_true = hasattr(importable, method)
        if is_true:
            method = getattr(importable, method)
            method()
        return is_true

    @staticmethod
    def print_package(package_list: List[str]):
        for index, packageName in enumerate(package_list):
            _, *packageWords = packageName.split('_')
            print("\t□ %d %s" % (index + 1, ' '.join(packageWords)))

    @staticmethod
    def read_menu(menu_path: str) -> int:
        """
            读取包名类的目录文件
        :param menu_path: 需要执行的个数
        :return:
        """
        limber: int = 0
        with open(menu_path, 'r', encoding='utf-8') as menuList:
            for line in menuList:
                print("\t□ " + line, end="")
                limber += 1
        print()
        return limber

    @staticmethod
    def is_exit(input_index: str or int) -> bool:
        """
            判断是否是退出
        :param input_index:
        :return:
        """
        return str(input_index).lower() == "e" or str(input_index).lower() == "q"

    @staticmethod
    def get_select_index(select_total: int) -> Tuple[bool, int]:
        """
            获取用户需要执行的方法索引
        :param select_total: 选择有多少方法的索引
        :return:
        """
        input_index = input("Please select a index what you want to execute programming[1-%d][e\\q exit]:" % select_total)
        is_select: bool = True  # 是否选择
        mes: str = "You enter the number is error"
        index: int = 0
        if ExecuteProgramForModule.is_exit(input_index):
            return is_select, index
        try:
            index = int(input_index)
            if index < 0 or index > select_total:
                print(mes)
                is_select = False
        except TypeError:
            print("You enter the number is error")
            is_select = False
        return is_select, index
