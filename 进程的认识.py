#! /usr/bin/python
# -*- coding: UTF-8 -*-

import multiprocessing
import os
import time

def test1(a):
    print("test1 start",a)
    print("test1的进程是：",os.getpid())
    print("test1的父进程是：",os.getppid())
def test2(a):
    print("test2 start", a)
    print("test2的进程是：", os.getpid())
    print("test2的父进程是：", os.getppid())
def main():
    print("main函数的进程是",os.getpid())
    a = multiprocessing.Process(target=test1,args=("hahah",))
    b = multiprocessing.Process(target=test2,args=("hahaha",))
    a.start()
    b.start()
    print("haha")
    pass


if __name__ == '__main__':
    main()