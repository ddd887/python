#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket

def main():
    s = socket.socket()
    s.bind(("",8999))
    s.listen(5)
    while True:
        c,addr = s.accept()
        print("%s is connecting"%(str(addr)))
        c.send("welcome".encode("utf-8"))
        while True:
              try:
                 date = c.recv(1024)
                 print(date.decode("utf-8"))
              except:
                  print("断开连接")
                  break
        c.close()
    s.close()
    pass



if __name__ == '__main__':
    main()