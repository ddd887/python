#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        text = input("你要发送的是：")
        s.sendto(text.encode("utf-8"),("192.168.179.1",8000))
        if text == 'exit':
            break
        ans = s.recvfrom(1024)
        print(ans[0].decode("utf-8"))
    s.close()

    pass

if __name__ == '__main__':
    main()