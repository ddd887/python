#! /usr/bin/python
# -*- coding: UTF-8 -*-


import random

def main():
    code = ''
    for i in range(4):
        ret = random.randint(0,9)
        add = chr(random.randint(65,90))
        num = random.choice([ret,add])
        code = ''.join([code,str(num)])
    print(code)
    pass



if __name__ == '__main__':
    main()