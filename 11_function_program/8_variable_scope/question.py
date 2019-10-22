#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-23
    Desc:Variable scope
"""
global_str = 'foo'
def test1():
    local_str = 'bar'
    print(global_str + local_str)

def foo():
    print("calling foo()...")
    bar = 200
    print("in foo(),bar is ",bar)
bar = 100
is_this_global = 'xyz'
def foo2():
    global is_this_global
    this_is_local = 'abc'
    is_this_global = 'def'
    print("this_is_local + is_this_global = ",this_is_local + is_this_global)
def test2():
    print("in __main__,bar is ",bar)
    foo()
    print("in __main__,bar is (still)",bar)
    print("is_this_global = ",is_this_global)
    foo2()
    print("is_this_global = ",is_this_global)
def foo3():
    m = 3
    def bar():
        n = 4
        print(m + n)
        def sar():
            k = 5
            print(m + n +k)
            def dar():
                l = 6
                print(m + n + k +l)
            print(k)
            dar()
        print(n)
        sar()
    print(m)
    bar()
def test3():
    foo3()
def counter(start_at = 0):
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]
    return incr
def test4():
    count = counter(5)
    print(count())
    print(count())
def test5():
    output = '<int %r id = %#0x val = %d>'
    w = y = x = z = 1
    def f1():
        x = y = z = 2
        def f2():
            y = z = 3
            def f3():
                z = 4
                print(output%('w',id(w),w))
                print(output % ('x', id(x), x))
                print(output % ('y', id(y), y))
                print(output % ('z', id(z), z))
            clo = f3.__closure__
            if clo:
                print("f3 closure vars:",[str(c) for c in clo ])
            else:
                print("no f3 closure vars")
            f3()
        clo = f2.__closure__
        if clo:
            print("f2 closure vars:", [str(c) for c in clo])
        else:
            print("no f2 closure vars")
        f2()
    clo = f1.__closure__
    if clo:
        print("f1 closure vars:", [str(c) for c in clo])
    else:
        print("no f1 closure vars")
    f1()
from time import time
def logged(when):
    def log(f,*args,**kargs):
        print("""Called function:%s
            args:%r
            kargs:%r"""%(f,args,kargs))
    def pre_logged(f):
        def wrapper(*args,**kargs):
            log(f,*args,**kargs)
            return f(*args,**kargs)
        return wrapper
    def post_logged(f):
        def wrapper(*args,**kargs):
            now = time()
            try:
                return f(*args,**kargs)
            finally:
                log(f,*args,**kargs)
                print("time delta:%s"%(time() - now))
        return wrapper
    try:
        return {
            "pre":pre_logged,
            "post":post_logged
        }[when]
    except KeyError as e:
        raise ValueError(e +'must be "pre" or "post"')
@logged("post")
def hello(name):
    print("Hello,"+name)

def test6():
    hello('world')

def test7():
    x = 10
    def foo():
        y = 5
        bar = lambda :x + y
        print(bar())
    foo()
def test8():
    j,k = 1,2
    def pro1():
        j,k = 3,4
        print("j == %d and k == %d"%(j,k))
        k = 5
    def pro2():
        j = 6
        pro1()
        print("j == %d and k == %d"%(j,k))
    k = 7
    pro1()
    print("j == %d and k == %d"%(j,k))
    j = 8
    pro2()
    print("j == %d and k == %d"%(j,k))