#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-21
    Desc:Formal paramter
"""
import  requests
def foo(who):
    """defined for only 1 argument"""
    print("Hello",who)

def taxMe(cost,rate = 0.0825):
    return cost + (cost * rate)

def test1():
    # foo()
    foo('World!')

# def taxMe2(rate = 0.0825,cost):

def test2():
    print(taxMe(100))
    print(taxMe(100,0.05))

def firstNotBlank(lines):
    for line in lines:
        if not line.strip():
            continue
        else:
            return line
def firstLast(webpage):
    """
    f = open(webpage)
    lines = f.readlines()
    f.close()
    """
    print(firstNotBlank(webpage))

def download(url = 'http://www',process = firstLast):
    try:
        retval = requests.get(url).text
        print(retval)
    except IOError:
        retval = None
    if retval:
        process(retval)

def test3():
    download("http://www.baidu.com")
if __name__ =="__main__":
    test3()
