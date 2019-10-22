#!/usr/bin/env python
# encoding = utf-8
"""
    @Author:Galois
    @Date:2018-12-3
    @Desc: method util
"""
import click

from utils.dazyimport import LazyImport
from utils.excute_package_method import ExecuteProgramForModule


def test():
    cname = "2_break_freewill_length_list_down.1_question"
    method = "test1"
    importable = LazyImport(cname, method)
    is_true = hasattr(importable, method)
    if is_true:
        method = getattr(importable, method)
        method()


@click.command()
@click.option("--execute_dir", default=__file__, help="执行所在的文件主目录")
@click.option("--file_name", prompt="Execute File Name:", help="执行的所在目录")
@click.option("--module_name", default="question", help="所要执行的模块文件名")
@click.option("--menu_file", default="menu.txt", help="所要执行的索引菜单文件名")
@click.option("--method_prefix", default="test", help="所要执行的方法名前缀")
def main(execute_dir: str, file_name: str, module_name: str = "question",
         menu_file: str = "menu.txt", method_prefix: str = "test") -> None:
    execute_for_module: ExecuteProgramForModule = ExecuteProgramForModule(execute_dir=execute_dir, file_name=file_name,
                                                                          module_name=module_name, menu_file=menu_file,
                                                                          method_prefix=method_prefix)
    execute_for_module.run()


if __name__ == "__main__":
    main()
