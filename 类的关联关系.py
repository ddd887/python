#! /usr/bin/python
# -*- coding: UTF-8 -*-


class boy:
    def __init__(self,name,girlfriend = None):
        self.name = name
        self.girlfriend = girlfriend
    def have_a_dinner(self):
           if self.girlfriend:
               print("%s和%s吃晚饭"%(self.name,self.girlfriend.name))
           else:
               print("单身狗，自己吃")
class girl:
    def __init__(self,name):
        self.name = name
def main():
    b = boy('日天')
    b.have_a_dinner()

    c = girl('如花')
    bb = boy('小明',c)
    bb.have_a_dinner()


    pass




if __name__ == '__main__':
    main()
