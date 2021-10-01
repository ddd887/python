#! /usr/bin/python
# -*- coding: UTF-8 -*-

class student:
    _num = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.addnum()
    @classmethod
    def addnum(self):
        self._num +=1
    @classmethod
    def getnum(self):
        return self._num
def main():
    st1 = student("xiaoming","18")
    st2 = student("xiaohong","19")
    st2 = student("xiaohei","20")

    print(student.getnum())
    pass


if __name__ == '__main__':
    main()
