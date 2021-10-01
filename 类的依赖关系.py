#! /usr/bin/python
# -*- coding: UTF-8 -*-

class elphant:
    def __init__(self,name):
        self.name = name
    def c(self,obj1):
        print(self.name+'开门了')
        obj1.a(self)
    def d(self,obj2):
        print(self.name+'关门了')
        obj2.b(self)




class door:
    def a(self):
        print(self.name+'冰箱门打开了')
    def b(self):
        print(self.name+'冰箱门关上了')
def main():
    ell = elphant('大象')
    hair = door()
    ell.c(door)
    pass


if __name__ == '__main__':
    main()