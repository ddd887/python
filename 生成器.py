#! /usr/bin/python
# -*- coding: UTF-8 -*-


def produce():
    for i in range(100):
        yield "生产了%s个包子"%i

def main():
    p = produce()
    num = 0
    for i in p:    #for i in range(12):
        print(i)    #     print(p._next_())
        num +=1
        if num == 12:
            break


    pass



if __name__ == '__main__':
    main()