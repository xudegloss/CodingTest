import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\python\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

N=int(input())
arr=[]

for i in range(N):
    arr.append(list(map(int, input().split())))


n=int(input())

# 1. 조건에 맞게 회전하기.

## Logic ##

# 왼쪽 0 기준 -> 잘라서 오른쪽에 붙이기.
# 오른쪽 마지막 인덱스 기준 -> 잘라서 왼쪽에 붙이기.

for iter in range(n):
    row, dt, move=map(int, input().split())

    if dt==0:
        arr[row-1] = arr[row-1][move: ] + arr[row-1][ :move]
    else:
        arr[row-1] = arr[row-1][ :N-1-move] + arr[row-1][N-1-move: ]

# arr는 회전을 마친 격자판을 의미한다.

# 2. 조건에 맞는 격자에서의 값을 구한 후 합계 구하기.
# top_res, mid_res, bottom_res

# top_res

iter=1
top_res=0

for i in range(N//2-1, -1, -1):
    top_res+=sum(arr[i][N//2-iter : N//2+iter+1])
    iter+=1


# mid_res

mid_res=arr[N//2][N//2]

# bottom_res

iter=1
bottom_res=0

for i in range(N//2+1, N):
    bottom_res+=sum(arr[i][N//2-iter : N//2+iter+1])
    iter+=1


# tot_res

tot_res = top_res + mid_res + bottom_res
print(tot_res)
