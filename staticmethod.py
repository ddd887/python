#! /usr/bin/python
# -*- coding: UTF-8 -*-

import time
class a:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    @staticmethod
    def b():
        return time.strftime("%H:%M:%S",time.localtime())
def main():
    print(a.b())
    pass


if __name__ == '__main__':
    main()