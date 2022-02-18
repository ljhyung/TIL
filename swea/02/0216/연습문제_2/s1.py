import sys
sys.stdin = open("input.txt", "r")


def itoa(num, string):
    check = False       # 음수 체크용
    if num < 0:
        num = -num
        check =True
    while num >0:
        string = chr(num%10+48) + string    # 앞에 1의 자리 글자 추가, chr(0)이 '0'이므로 48추가
        num //= 10                          # 변환한 1의 자리 날리기
    if check:
        string = '-' + string
    print(string, type(string))

for i in range(6):
    num = int(input())
    string = ''
    print(f'#{i+1}', end=' ')
    itoa(num, string)
