#!/usr/bin/env python
# coding=utf-8
"""
    Author:Galois
    Date:2018-12-15
    Desc:Invoking function
"""
from operator import add,sub
from random import randint,choice
ops = {'+':add,'-':sub}
MAXTRIES = 2
def doprob():
    symbol = ''
    op = choice('+-')
    nums = [randint(1,10) for i in range(len(ops.keys()))]
    nums.sort(reverse=True)
    print(nums)
    ans = ops[op](*nums)
    pr = '%d %s %d = '%(nums[0],op,nums[1])
    oops = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print('correct')
                break
            if oops == MAXTRIES:
                print("answer\n%s%d"%(pr,ans))
            else:
                print('incorrect...try again')
                oops += 1
        except (KeyboardInterrupt,EOFError,ValueError) as e:
            print("Invalid input...try again")
def main():
    while True:
        doprob()
        try:
            opt = input("Again?[y]").lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt,EOFError) as e:
            break

def test1():
    """算术游戏"""
    main()

if __name__ == "__main__":
    main()