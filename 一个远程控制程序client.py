#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import os

def main():
    s = socket.socket()
    host = '192.168.179.1'
    port = 12345
    s.connect((host,port))
    while True:
        date_recv = s.recv(1024)
        print(date_recv.decode("utf-8"))
        msg = input("你要输入的是：")
        s.send(msg.encode("utf-8"))
    s.close()
    pass



if __name__ == '__main__':
    main()
