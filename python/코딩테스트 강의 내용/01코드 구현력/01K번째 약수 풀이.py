import sys
import os

current_path=os.getcwd() # 현재 작업 디렉토리 경로 얻어오기.
sys.stdin=open(current_path + "\\python\\코딩테스트 강의 내용\\01코드 구현력\\" + "input.txt", "rt")

input= list(map(int, input().split()))
N=input[0]
K=input[1]

_list=[]
for num in range(1, N+1):
    if N%num==0:
        _list.append(num)

if len(_list)<K:
    print(-1)
else:
    print(_list[K-1])


# N, K = map(int, input().split())

"""
cnt=0
for i in range(1, N+1):
    if n%i==0:
        cnt+=1
    if cnt==K:
        print(i)
        break
else:
    print(-1)
"""
