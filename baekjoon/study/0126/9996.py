N = int(input())
a, b = list(map(str, input().split('*')))

# for _ in range(N):
#     str = input()
#     if len(str) < (len(a)+len(b)):
#         print('NE')
#     elif str[:len(a)] == a and str[-len(b):] == b:
#         print('DA')
#     else:
#         print("NE")

for _ in range(N):
    str = input()
    if len(str) < (len(a)+len(b)):
        print('NE')
    elif str.startswith(a) and str.endswith(b):     # 메서드 잘 쓰자
        print('DA')
    else:
        print("NE")