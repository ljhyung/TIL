'''
https://www.acmicpc.net/problem/2812
크게 만들기
골드3
2시간
'''

N, K = map(int, input().split())
num = list(map(int,input()))
answer = []
cnt=0
def search():
    global cnt, answer
    for i in range(N):
        if cnt==K or len(answer)==0:
            answer.append(num[i])
            continue
        while num[i]>answer[-1]:
            answer.pop()
            cnt +=1
            if cnt==K:
                answer = answer+[*num[i:]]
                return
            if len(answer)==0:
                break
        answer.append(num[i])


search()


print(''.join(map(str,answer[:-(K-cnt)])))