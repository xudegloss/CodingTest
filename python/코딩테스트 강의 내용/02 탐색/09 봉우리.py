import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\python\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

# 1. 가장자리에 0이 있게 격자판을 제작하기.

N=int(input())
arr=[[0]*(N+2)]

for i in range(N):
    arr.append([0] + list(map(int, input().split())) + [0])
arr.append([0]*(N+2))

# 2. 상하좌우를 탐색한 후에 상하좌우보다 큰 경우 봉우리라고 생각하고 카운팅한다.

cnt=0

for i in range(1, N+1):
    for j in range(1, N+1):
        top_row, top_col = i-1, j
        left_row, left_col = i, j-1
        right_row, right_col = i, j+1
        bottom_row, bottom_col = i+1, j
        if (arr[i][j]>arr[top_row][top_col]) and (arr[i][j]>arr[left_row][left_col]) and (arr[i][j]>arr[right_row][right_col]) and (arr[i][j]>arr[bottom_row][bottom_col]):
            cnt+=1

print(cnt)