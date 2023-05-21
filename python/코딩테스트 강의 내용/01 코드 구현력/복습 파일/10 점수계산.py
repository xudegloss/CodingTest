import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N=int(input())
arr=list(map(int, input().split()))
result=[0]*N

for idx in range(N):
    if arr[idx]==0:
        result[idx]=0
    else: # arr[idx]==1, 정답인 경우
        result[idx]=1
        if arr[idx-1]==1:
            result[idx]=(result[idx-1]+1)

print(sum(result))