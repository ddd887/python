#! /usr/bin/python
# -*- coding: UTF-8 -*-

def func1(fun):
    def inner(*args,**kwargs):
        fun(*args,**kwargs)
    return inner


@func1
def fun1(*args,**kwargs):
    print(args,kwargs)

def mian():
    fun1('a','b',1,2,3,age="18",name="xiaoming")
    pass




if __name__ == '__main__':
    mian()