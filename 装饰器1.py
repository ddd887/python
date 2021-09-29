#! /usr/bin/python
# -*- coding: UTF-8 -*-

import time


def fun2(fun):
    def inner():
        start = time.time()
        fun()
        print(time.time()-start)
    return inner

@fun2
def fun1():
    time.sleep(3)
    print("whoami")


def main():
    fun1()




    pass




if __name__ == '__main__':
    main()