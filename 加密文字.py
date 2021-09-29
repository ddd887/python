#! /usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib

def main():
    md5 = hashlib.md5()
    t = input("你要加密的是：")
    md5.update(("t").encode('utf-8') )
    print(md5.hexdigest())
    pass



if __name__ == '__main__':
    main()