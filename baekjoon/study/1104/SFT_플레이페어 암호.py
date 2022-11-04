'''
https://softeer.ai/practice/info.do?idx=1&eid=804
플레이페어 암호
난이도 3/5

'''

import sys

msg = input()
key = input()
keyList = list(key)
keyLen = len(key)
alpha = [0 for _ in range(26)] #-65
alpha[9]=1
msgTran = []

lst = [[" " for _  in range(5)] for _  in range(5)]
cnt = 0
for r in range(5):
    for c in range(5):
        while cnt<keyLen:
            if alpha[ord(keyList[cnt])-65]==0:
                lst[r][c] = keyList[cnt]
                alpha[ord(keyList[cnt])-65]=1
                cnt += 1
                break
            else:
                cnt +=1
        else:break
cnt=0
for r in range(5):
    for c in range(5):
        if lst[r][c]==" ":
            while cnt<26:
                if alpha[cnt]==0:
                    lst[r][c] = chr(cnt+65)
                    alpha[cnt]=1
                    cnt += 1
                    break
                else:
                    cnt += 1
            else:break

# 이동 편하게 dict
alphaDict = dict()
for r in range(5):
    for c in range(5):
        alphaDict[lst[r][c]] = [r,c]

head = 0
while head<len(msg):
    if head == len(msg) - 1:
        front = msg[head]
        rear = "X"
        msgTran.append([front,rear])
        break
    else:
        front = msg[head]
        rear = msg[head+1]
        if front==rear:
            if front=="X":
                rear="Q"
                head-=1
            else:
                rear = "X"
                head-=1
        msgTran.append([front,rear])
        head+=2
# print(msgTran)
######################## 메세지 구현 완료
######################## 이동 시작
answer = []
for two in msgTran:
    front = alphaDict.get(two[0])
    rear = alphaDict.get(two[1])

    # 행이 같을 때
    if front[0]==rear[0]:
        answer.append(lst[front[0]][(front[1]+1)%5])
        answer.append(lst[rear[0]][(rear[1]+1)%5])
    elif front[1]==rear[1]:
        answer.append(lst[(front[0] + 1) % 5][front[1]])
        answer.append(lst[(rear[0] + 1) % 5][rear[1]])
    else:
        answer.append(lst[front[0]][rear[1]])
        answer.append(lst[rear[0]][front[1]])

print("".join(answer))


# print(lst)









































