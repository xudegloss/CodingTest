import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "//python//코딩테스트 강의 내용//01 코드 구현력//" + "input.txt")

N=int(input())
arr=[0]*N
cnt=0

for n in range(2, N+1):
    if arr[n-1]==0:
        cnt+=1
        for i in range(n, N+1, n):
            arr[i-1]+=1

print(cnt)

"""
ch=[0]*(N+1)
cnt=0

for i in range(2, N+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, N+1, i):
            ch[j]=1
print(cnt)

"""