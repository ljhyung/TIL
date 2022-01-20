import sys

lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int, input().split())
    print(A + B)
# sys.stdin.readlines() 를 이용해 파일의 끝 부분까지 한번에 가져온다

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break
# # while 문에서 입력이 없으면 종료되지 않을 떄 eof(end of file)에러가 떠서 끝을 판단하는 방법으로 try except를 사용

