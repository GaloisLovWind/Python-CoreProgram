# 核心编程中代码练习项目

## 项目结构
* `app.py` 为项目主入口文件 
* `python app.py --file_name=11_function_program` 为执行命令； 其中 file_name 为你要执行的包所在
文件目录，然后根据你要执行的包所在的输入对应索引进行运行对应的方法; e 或者 q 标识退出程序
* `tests` 文件夹为所在的测试目录
* `requitements.txt` 为项目所需要的模块依赖
* `utils` 公共模块目录
* `ReadMe.md` 为说明文件
* 其他的文件夹为学习文件目录入口文件
    * `menu.txt` 为此包类的所有方法的说明索引文件
    * `question.py` 为执行的的所有方法模块文件，方法名以 `test + index`
    实现运行入口

## 学习内容
### Python 起步
1. print 方法调用 str() 函数显示对象，交互式解释器则调用 repr() 函数显示对象
2. 运算符中 特有运算符`//` 为整除运算符， `**` 幂运算； `and or not` 为逻辑运算符
3. 变量名为大小写敏感，可不需要预先声明变量类型， 在3.5版本之后启用了类型提示
 复杂类型可使用 `typing` 模块中声明变量类型
4. 字符串特有规则： 第一个字符的索引是 0，最后一个字符的索引是 -1；
    \+ 用于字符串连接， \* 用于字符串重复
5. 元组为只读列表，不能更改
6. 函数如果没有 return 语句，就会自动返回 None 对象； 定义函数脚本
    ```buildoutcfg
    def function_name([arguments]):
        """optional documents string"""
        funtion_suite
    ```
7. 类，如果没有标明基类，则默认使用 object 作为基类；定义类：
    ```buildoutcfg
    class ClassName(base_class[es]):
       """ optional documentation string """
       static_member_declarations
       method_declarations
    ```
   `__init__` 并不是创建实例，只是对象创建实例后执行的第一个方法，目的是
   执行一些对象的必要的初始化工作， self 为类实例自身的引用 
### Python 基础
1. \\ 为换行分隔；不同的缩进分隔不同的代码块； \; 为同一行多个语句隔开符
2. 增量运算符（+=，-=，%=等）第一个对象仅被处理一次。可变对象会被就地修改（
无修拷贝引用），不可变对象则结果一样（分配一个新对象）
3. 标识符规则：
    * 第一个字符必须是字母或者下划线 (_)
    * 剩下的字符可以是数字或字母或下划线
    * 大小写敏感
4. 关键字的查阅可在 keyword 模块进行
5. 专用下划线的标识符
    * _xxx 不用 `from module import *` 导入，即是模块内私有的变量名和方法名
    * \_\_xxx\_\_ 系统定义名字
    * __xxx 类中私有变量名
6. obj.\_\_doc__ 动态获取 obj 的文档字符串（obj 可为对象、函数、模块）
7. 模块结构和布局
    + （1） 起始行（Unix） 通常只有类Unix 环境使用
    + （2） 模块文档  简要介绍模块功能及重要变量定义，可通过 module.\_\_doc__访问
    + （3） 模块导入  导入当前模块所需所有模块：每个模块仅导入一次，函数内部导入不会被执行
    + （4） 变量定义  全局变量定义
    + （5） 类定义   通过module.class 在外部调用，可通过 class.\_\_doc__ 文档定义
    + （6） 函数定义  通过module.function() 在外部调用，可通过 function.\_\_doc__ 文档定义
    + （7） 主程序   执行当前模块方法
    模板例子
    ```buildoutcfg
    #! /usr/bin/env python
    " this is a test module "
    import sys
    import os
    debug = True
    class FooClass(object):
       " Foo class"
       pass
    def test():
       " test function" 
       foo = fooClass()
       if debug:
           print("run test()")
    if __name__ == "__main__":
       test()
    ```
8. `__name__` 系统变量，如果模块被导入，则 `__name__`的值为模块名字；如果
模块是被直接执行， `__name__` 的值为 `__main__`
9. 内存管理
    * 动态类型 对象的类型和内存占用都是运行时确定
    * 引用计数 一个内部跟踪变量，称为一个引用计数器，每个对象各有多少引用，简称引用计数；当对象被
    创建时，创建一个引用计数，当这个对象不再需要，即这个对象的引用计数变为0时，它被垃圾回收；当一
    个对象被创建并将其引用赋值给变量时，该对象的引用计数被设置为1.当对象引用被销毁时，引用计数会
    减少
    * del 语句  会删除对象一个引用；从现在的名字空间中删除 或者 该对象的引用计数建议减一
    * 垃圾收集
### Python 对象
1. 对象的布尔值为False规则：
    * None 
    * False
    * 所有的值为零的数
    * 空字符串 ""
    * 空列表 []
    * 空元组 ()
    * 空字典 {}
    * 用户创建的类如果定义了nonzero(\_\_nonzero__() Python3 不支持此方法，换成 \_\_bool__) 或 length(\_\_len__())且值为0
2. 对象比较： `aobj is bobj` 等价于 `id(aobj) == id(bobj)`
3. 数据类型分类：
    1. 可变类型： List, Dict
    2. 不可变类型： int， str， Tuple
    
    访问类型分类：
    1. 直接访问: int
    2. 顺序访问: str, List, Tuple
    3. 映射访问: Dict
4. 
### Python 数字
1. 复数的实部和虚部默认为浮点型（Float）
2. \+ 运算符；当两个操作数的数据类型不同时，则根据两个操作数的存在的数据类型 `complex > float > int > bool`
的优先顺序进行转换 
3. bool 对类的转换，根据 \_\_bool__ 和 \_\_len__ 的方法实现完成，

















## 附录A：pip 常用命令
1. `python -m pip install --upgrade pip` 更新 pip
2. `pip install -r requirements.txt` 安装 requirements.txt 中的模块

## 附录B: 常用的全局函数
>        dir([obj]) # 显示对象属性，如果没有提供参数，则显示全局变量的名字
>        help([obj]) # 显示对象的文档字符串， 如果没有提供任何参数，则进入交互式帮助
>        int(obj) # 将一个对象转换成为整数
>        len(obj) # 返回对象长度
>        open(fn, mode) # 以 mode('r'=read, 'w'=write) 方式打开一个文件名为fn 的文件
>        range([star,]stop[, step]) 返回一个整数列表对象，起始值为 start ，
>        结束值为 stop - 1， start 默认值为 0， step 默认值为 1
>        input(str) # 等待用户输入一个字符串， 可选参数 str: 提示信息
>        str(obj)  # 将一个对象转换为字符串
>        type(obj) # 返回对象类型(返回值本身是一个 type 对象）
>        cmp(obj1, obj2) （python3不存在，在operator模块类似用法）比较 obj1 和 obj2 ，调用对象的内部方法__cmp__方法 根据比较结果返回整数i: i < 0 if obj1 < obj2
>        repr(obj) 返回对象的字符串表示
>        id(obj) 获取唯一标识ID，可用来区分可变类型和不可变类型