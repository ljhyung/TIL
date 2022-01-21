nums = [int(input()) for _ in range(9)]
mx = nums[0]
cnt = 0
rw = 0

for num in nums:
    cnt +=1
    if mx <= num:
        mx = num
        rw = cnt
print(mx)
print(rw)