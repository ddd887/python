#! /usr/bin/python
# -*- coding: UTF-8 -*-

from collections import Iterable

def main():
    I = [1,2,3,4]
    a = {1,2,3,4}
    b = (1,2,3,4)
    c = {1:2,3:4,5:6}
    print(isinstance(I,Iterable))
    pass



if __name__ == '__main__':
    main()
