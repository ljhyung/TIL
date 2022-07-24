from socket import *
from threading import Thread
import time

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8081 #통신할 대상의 Port 주소

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port)) # #서버로 연결시도

print('접속 완료')
res = ''
sender = Thread(target=send, args=(clientSock,))
receiver = Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

if res == 'quit':
    clientSock.close()

while True:
    time.sleep(1)
    pass