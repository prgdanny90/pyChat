#-*- coding: utf-8 -*-
# chat_client.py

from socket import *

def setAddress() :
    host = "127.0.0.1"
    print u"포트를 입력하세요 : "
    port = int(raw_input())

    return (host, port)

def main() :
    print "###############"
    print u"대화방"
    print "###############"

    # 서버 소켓 생성
    addr = setAddress()
    print addr
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(addr)
    server.listen(1)

    # 클라이언트를 받아들인다.
    client, add = server.accept()

    print addr
    # 데이터를 주고 받는다.
    name = client.recv(10)
    send_data = "***" + name + u"님께서 접속하셨습니다. ***"
    while send_data:
        print send_data
        ### TODO UTF8 데이터 왔다리 갔따리 안됨 ###
        client.send(send_data)
        send_data = name + '] ' + client.recv(1024)

if __name__ == '__main__':
    main()
