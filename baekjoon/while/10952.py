while True:
    A, B = map(int, input().split())
    if not (A or B):
        break
    print(A+B)
