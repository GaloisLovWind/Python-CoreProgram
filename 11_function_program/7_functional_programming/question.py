#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-22
    Desc:Functional programming
"""
from functools import reduce,partial
from random import randint
from operator import add,mul
import tkinter
def odd(n):
    return n % 2
def test1():
    a = lambda x, y = 2 :x + y
    print(a(3))
    print(a(3,5))
    print(a(0))
    print(a(0,9))
    b = lambda *z:z
    print(b(23,'zyx'))
    print(b(42))

def test2():
    """內建函数：apply(),filter(),map(),reduce()"""
    # filter  first building
    allNums = []
    for eachNum in range(9):
        allNums.append(randint(1,99))
    print([i for i in filter(odd,allNums)])
    # filter second building
    allNums = filter(lambda n:n % 2,[randint(1,99) for eachNum in range(9)])
    print(list(allNums))
    # filter third building
    print([n for n in [randint(1,99) for i in range(9)] if n % 2])
    # map one list
    print(list(map(lambda x : x + 2,[0,1,2,3,4,5])))
    print(list(map(lambda x: x ** 2,range(6))))
    print([n + 2 for n in range(6)])
    print([n ** 2 for n in range(6)])
    # map more than one list
    print(list(map(lambda x,y: x + y,range(6),range(6))))
    print(list(map(lambda x,y:(x + y ,x - y ),range(6),range(6))))
    # print(list(map(None,[1,2,3],[4,5,6])))
    # reduce Don't use reduce function
    allNums = range(5)
    total = 0
    for eachNum in allNums:
        total = mySum(eachNum,total)
    print("the total is:",total)
    # reduce
    print("the total is:",reduce(mySum,allNums))
    print("the total is:",reduce(lambda x,y:x+y,allNums))
def mySum(x,y):
    return x + y
def test3():
    add1 = partial(add,1)
    mul100 = partial(mul,100)
    print(add1(10))
    print(add1(1))
    print(mul100(100))
    print(mul100(500))

def test4():
    root = tkinter.Tk()
    myButton = partial(tkinter.Button,root,fg = 'white',bg = 'blue')
    b1 = myButton(text = 'Button 1')
    b2 = myButton(text = 'Button 2')
    qb = myButton(text = 'QUIT', bg = 'red',command = root.quit)
    b1.pack()
    b2.pack()
    qb.pack(fill = tkinter.X,expand = True)
    root.title('PFAs')
    root.mainloop()