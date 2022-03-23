import sys
sys.stdin = open("input.txt", "r")

pattern = {
    '0001101': '0',
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = ''
    for _ in range(N):
        temp = input()
        if '1' in temp and not num:     # 유의미한 입력만 저장
            num = temp
    res = []
    num = num[::-1]                     # 암호들의 시작값은 정해지지 않지만 끝 값은 1이므로 뒤에서부터 탐색
    i = num.index('1')                  # 뒤집히기전 마지막이자 뒤집힌 후는 첫 번째 암호가 시작하는 인덱스
    while i < len(num) and len(res)<8:  # 패턴 매칭
        temp = num[i:i+7][::-1]               # 7자리 슬라이싱 후 뒤집기
        temp = pattern.get(temp)        # 딕셔너리 get
        if temp:
            res.append(int(temp))       # value가 존재하면 res에 추가
            i += 7                      # 매칭한 패턴 다음을 검사
        # else:
        #     i += 1                      # 매칭 패턴 없으면 다음 차례로이나 이 부분은 필요 없을듯
    cnt = 0
    res = res[::-1]
    for k in range(4):
        cnt += 3*res[2*k] + res[2*k+1]  # 조건 부합하는지 검사
    result=0
    if not cnt%10:
        result = sum(res)
    print(f'#{tc} {result}')
