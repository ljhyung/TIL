'''
BOJ
파일 합치기
골드 3

https://www.acmicpc.net/problem/11066
'''
T = int(input())
for tc in T:
    K = int(input())
    lst = list(map(int, input().split()))
    dp = [[0 for _ in range()] for _ in range()]