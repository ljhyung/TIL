import sys
sys.stdin = open("input.txt", "r")


tc = int(input())
def check(lst, numlst):
    global check_lst
    for i in range(0, len(lst), 4):         # 빈칸 포함 4글자씩 건너띄기
        for k in range(len(numlst)):
            if numlst[k] == lst[i:i+3]:     # 3글자 체크
                check_lst[k] += 1           # 값에 해당하는 인덱스에 증가
                break
    return

numlst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for i in range(tc):
    check_lst = [0 for _ in range(10)]
    tcn, N = input().split()
    lst = input()
    check(lst, numlst)
    string = ''
    print(tcn)
    for j in range(10):
        string += (numlst[j]+' ')*check_lst[j]
    print(string[:-1])



# def findx(j):     # 선택 정렬로 만들어 봤는데 검사를 너무 많이 해서인지 결과가 뜨는데 한참 걸려서 다른 방법으로
#     check = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     for i in range(len(check)):
#         if check[i] == j:
#             break
#     return i
#
# def sortidx(lst, start):
#     for k in range(start, len(lst)):
#         if findx(lst[start]) > findx(lst[k]):
#             lst[start], lst[k] = lst[k], lst[start]
#     return
#
# tc = int(input())
# check = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# for i in range(tc):
#     tcn, N = input().split()
#     lst = list(input().split())
#     for j in range(len(lst)):
#         sortidx(lst, j)
#     print(tcn)
#     print(lst)




# tc = int(input())                     # 그냥 갯수 세서 곱하기
# def check(lst, word):
#     cnt = 0
#     for i in range(0, len(lst)-len(word),4):
#         for k in range(len(word)):
#             if word[k] != lst[i+k]:
#                 break
#         else:
#             cnt += 1
#     return cnt
#
# numlst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# for i in range(tc):
#     tcn, N = input().split()
#     lst = input()
#     string = ''
#     print(tcn)
#     for j in range(10):
#         string += (numlst[j]+' ')*check(lst,numlst[j])
#     print(string[:-1])


