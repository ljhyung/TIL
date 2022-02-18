import sys
sys.stdin = open("input.txt", "r", encoding='UTF8')

for i in range(10):
    tc = int(input())
    fs = input()
    string = input()
    cnt = 0
    for j in range(len(string)-len(fs)+1):      # +1 범위 잘 살피기
        for k in range(len(fs)):
            if fs[k] != string[j+k]:            # 다르면 break
                break
        else:                                   # break없이 종료 되면 문자열이 있으므로 cnt 증가
            cnt += 1
    print(f'#{tc} {cnt}')
