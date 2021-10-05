#! /usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import sys

def open(ip,port):
    s = socket.socket()
    try:
        s.connect((ip,port))
        return True
    except:
        return False
def scan(ip,portlist):
    for x in portlist:
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port close" % (ip, x))
def rescan(ip,s,e):
    for x in range(s,e):
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port close" % (ip, x))
def main():
    defaultport = [135,139,445,1433,3306,3389,5944]

    if len(sys.argv) == 2:
        str = sys.argv[1]
        if str[0] == '-':
            option = sys.argv[1][1:]
            if option == 'version':
                print("该版本是2017")
            elif option == 'help':
                print("python xxx.py [ip] [port:89,99,80或80-99]")
            sys.exit()
        scan(sys.argv[1],defaultport)
    elif len(sys.argv) == 3:
        if ',' in sys.argv[2]:
            p = sys.argv[2]
            p = p.split(',')
            a = []
            for x in p:
                a.append(x)
            scan(sys.argv[1],a)
        if '-' in sys.argv[2]:
            a = sys.argv[2]
            a = a.split('-')
            s = int(a[0])
            e = int(a[1])
            rescan(sys.argv[1],s,e)



    pass


if __name__ == '__main__':
    main()







