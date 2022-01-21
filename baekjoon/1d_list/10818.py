N = int(input())
nums = list(map(int, input().split()))
mx = nums[0]
mn = nums[0]

for num in nums:
    if mx < num:
        mx = num
    if mn > num:
        mn = num
print(mn, mx)

