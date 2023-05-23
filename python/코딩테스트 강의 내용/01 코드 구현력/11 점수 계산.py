import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "//python//코딩테스트 강의 내용//01 코드 구현력//" + "input.txt")

N=int(input())
arr=list(map(int, input().split()))
result=[0]*N

for idx in range(N):
    if arr[idx]==0:
        result[idx]=0
    elif arr[idx]!=0 and arr[idx-1]==0:
        result[idx]=1
    elif arr[idx]!=0 and arr[idx-1]!=0:
        result[idx]=(result[idx-1]+1)

print(sum(result))

"""
## 가중치와 합계를 이용하여 풀이하기.

sum=0 # 합계
cnt=0 # 가중치

for x in arr:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0

print(sum)
"""