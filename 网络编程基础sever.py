#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket

def main():
     s = socket.socket()
     port = 12345
     host = socket.gethostname()
     s.bind((host,port))
     s.listen(5)
     c,addr = s.accept()
     print("对方的地址是",addr)
     c.send('welcome'.encode("utf-8"))
     print(c.recv(1024).decode("utf-8"))
     c.close()

     pass


if __name__ == '__main__':
    main()
