import sys
sys.stdin = open("input.txt", "r")

def rev(string):
    lst = []
    for i in range(len(string)-1,-1,-1):    # 뒤에서부터 새 리스트에
        lst.append(string[i])
    return ''.join(lst)


tc = int(input())
for i in range(tc):
    string = input()
    print(f'#{i+1} {rev(string)}')


def strlen(a):          # 교재에 있어서 만들어 봤습니다
    i = 0
    cnt = 0
    while a[i] != '\0':
        cnt += 1
        i += 1
    return cnt


a = ['a', 'b', 'c', '\0']
print(strlen(a))