#-*- coding: utf-8 -*-
# chat_client.py
# Socket Docs url : 
# https://docs.python.org/2/library/socket.html
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
	print u"대화명을 입력하세요 : "

	name = raw_input()

	addr = setAddress()

	"""
	AF_INET : 인터넷 어디든 존재가능
	AF_UNIX : 유닉스 환경의 동일한 컴퓨터에 존재가능
	"""
	"""
	SOCK_STREAM : TCP 소켓 생성
	SOCK_DGRAM : UDP 소켓 생성
	"""
	client = socket(AF_INET, SOCK_STREAM)
	# 튜플로 인식 시키기 위해 소괄호 한번더
	client.connect(addr)

	# 서버에게 내 아이디 알려주기
	client.send(name)
	# 서버에게 내 아이디 알려준뒤 환영 메시지 받기
	recv_data = client.recv(100)
	# 반복하여 서버에서 입력 데이터 보내고 / 데이터 받기
	while True:
		print recv_data
		# 엔터만 눌렀을때 서버의 대답만 기다리며 먹통이 되는 케이스 막기
		client.send(raw_input() or ' ')
		recv_data = client.recv(1024)

if __name__ == '__main__':
	main()