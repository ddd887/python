#! /usr/bin/python
# -*- coding: UTF-8 -*-

import time


def fun2(fun):
    def inner(a):
        start = time.time()
        fun(a)
        print(time.time()-start)
    return inner

@fun2
def fun1(a):
    time.sleep(3)
    print("whoami")
    print(a)


def main():
    fun1(5)




    pass




if __name__ == '__main__':
    main()