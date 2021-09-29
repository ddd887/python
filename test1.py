#! /usr/bin/python
# -*- coding: UTF-8 -*-

c = 100
def fun1():
    global c
    c = c+2
    print(c)



def main():
    fun1()
    pass



if __name__ == '__main__':
    main()








