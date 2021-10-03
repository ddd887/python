#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket

def main():
    s = socket.socket()
    host = '192.168.179.1'
    port = 12345
    s.connect((host,port))
    msg = input("你要发送的是")
    s.send(msg.encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))
    s.close()
    pass

if __name__ == '__main__':
    main()
