#! /usr/bin/python
# -*- coding: UTF-8 -*-


class people:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    @property
    def a(self):
        return self.weight/(self.height**2)

def main():
    b = people('xiaoming','18',10,20)
    print(b.a)
    pass

if __name__ == '__main__':
    main()