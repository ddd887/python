#! /usr/bin/python
# -*- coding: UTF-8 -*-

def fun1(flag):
    def inner(fun):
        def hei(a):
            if flag:
                print("函数开始执行")
                fun(a)
                print("函数结束执行")
            else:
                print("请开启flag")
        return hei
    return inner
@fun1(True)
def fun2(a):
    print("haha----",a)

def main():
    fun2("nihao")

    pass


if __name__ == '__main__':
    main()