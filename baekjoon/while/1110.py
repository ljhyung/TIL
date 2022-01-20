num = int(input())
k = None
temp = 0
cnt = 0
while k != num:
    if cnt == 0:
        k = num
    cnt +=1
    temp = (k//10 + k%10)
    if temp>=10:
        temp = temp%10
    k = int((k%10)*10 + temp)

print(cnt)
