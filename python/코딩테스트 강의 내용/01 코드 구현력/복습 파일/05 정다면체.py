import sys
import os

current__path=os.getcwd()
sys.stdin=open(current__path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N, M=map(int, input().split())
count_arr=[0]*(N+M+3)

for i in range(1, N+1):
    for j in range(1, M+1):
        count_arr[i+j]+=1


max_count=max(count_arr)

for idx in range(0, len(count_arr)):
    if count_arr[idx]==max_count:
        print(idx, end=" ")