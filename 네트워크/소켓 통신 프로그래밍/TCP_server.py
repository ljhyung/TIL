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
        # if recvData.decode('utf-8') == 'quit':




port = 8081 #수신받을 Port

serverSock = socket(AF_INET, SOCK_STREAM) # AF_INET은 IPv4, TCP SOCK_STREAM
serverSock.bind(('', port)) #소켓에 수신받을 IP주소와 PORT를 설정, ''은 모든 인터페이스와 연결
serverSock.listen(1) #소켓 연결, 여기서 파라미터는 접속수를 의미

print(f'{port}번 포트로 접속 대기 중...')

connectionSock, addr = serverSock.accept() #해당 소켓을 열고 대기

print(str(addr), '에서 접속되었습니다.')

res = ''
sender = Thread(target=send, args=(connectionSock,))
receiver = Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

if res == 'quit':
    print('연결을 종료합니다')
    serverSock.close()

while True:
    time.sleep(1)
    pass

    

