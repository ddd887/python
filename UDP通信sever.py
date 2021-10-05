#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(("",8000))
    while True:
        date, addr = s.recvfrom(1024)
        print("connect by:", addr)
        print("recv date:",date.decode("utf-8"))
        s.sendto(date,addr)
    s.close()

    pass


if __name__ == '__main__':
    main()