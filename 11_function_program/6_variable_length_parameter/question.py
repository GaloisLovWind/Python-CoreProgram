#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-22
    Desc:Variable length paramter
"""

def tupleVarArgs(arg1,arg2 = 'defaultB',*theRest):
    'display regular args and non-keyword variable args'
    print("formal arg 1:",arg1,'formal arg 2:',arg2 )
    for eachXtrArg in theRest:print("another arg:",eachXtrArg)
def dictVarArgs(arg1,arg2 = 'defualtB',**theRest):
    'display 2 regular args and keyword variable args'
    print("formal arg 1:",arg1)
    print("formal arg 2:",arg2)
    for eachXArg in theRest.keys():print('Xtra arg %s:%s'%(eachXArg,str(theRest[eachXArg])))
def newfoo(arg1,arg2,*nkw,**kw):
    'display regular args and all variable args'
    print("arg1 is:",arg1,"arg2 is:",arg2)
    for eachNKW in nkw:print("additional non-keyword arg:",eachNKW)
    for eachKW in kw.keys():print("additional keyword arg '%s':%s"%(eachKW,kw[eachKW]))

def testit(func,*nkwargs,**kwargs):
    try:
        retval = func(*nkwargs,**kwargs)
        result = (True,retval)
    except Exception as diag:
        result = (False,str(diag))
    return result

def test1():
    tupleVarArgs('abc')
    tupleVarArgs(23,4.56)
    tupleVarArgs('abc',123,'xyz',456.789)
def test2():
    dictVarArgs(1220,740.0,c = 'grail')
    dictVarArgs(arg2 = 'tables',c = 123,d = 'poe',arg1 = 'mystery')
    dictVarArgs('one',d = 10,e = 'zoo', men = ('freud','gaudi'))
    newfoo('wolf',3,'projects',freud = 90,gramble = 96)
    aTuple = (6,7,8)
    aDict = {'z':9}
    newfoo(1,2,3,x = 4,y = 5,*aTuple,**aDict)
def test3():
    funcs = (int,float)
    vals = (1234,12.34,'1234','12.34')
    for eachFunc in funcs:
        print("-"*20)
        for eachVal in vals:
            retval = testit(eachFunc,eachVal)
            print("%s(%s)=" % (eachFunc.__name__, eachVal),end = ' ')
            if retval[0]:
                print(retval[1])
            else:
                print("FAILED:",retval[1])
if __name__ == "__main__":
    print(*{'x':1})