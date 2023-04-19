# 재귀함수와 스택
## 반복문 대체제 : 재귀함수 (자기 자신을 계속 호출)

import sys
n=int(sys.stdin.readline())

def DFS(x):
    if x>0:
        DFS(x-1)
        print(x)
DFS(n)