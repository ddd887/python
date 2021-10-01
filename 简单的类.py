#! /usr/bin/python
# -*- coding: UTF-8 -*-


class human:
    def __init__(self,name,sex,age,job):
        self.name = name
        self.sex = sex
        self.age = age
        self.job = job
    def work(self):
            print(self.name+"会工作")
    def tools(self):
            print(self.name+"会使用工具")
def main():
    obj = human('小明','boy','18','driver')
    print(obj.name)
    obj.work()
    obj.money = 100
    print(obj.money)
    obj.tools()


    pass



if __name__ == '__main__':
    main()