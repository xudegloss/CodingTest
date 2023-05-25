import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\python\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

N=int(input())
res=[]

# 각 행의 값을 모두 가져와서 이차원 격자판 행렬 만들기.

for idx in range(N):        
    res.append(list(map(int, input().split())))

# 각 행 별로 더하여 최대값 찾기. 

row_max=-21470000000

for i in range(N):
    mid_res_row=sum(res[i])
    if mid_res_row>row_max:
        row_max=mid_res_row

col_max=-21470000000
mid_res_col=0

standard=0
while standard<N:
    mid_res_col=0
    for j in range(N):
        mid_res_col+=res[j][standard]
    if mid_res_col>col_max:
        col_max=mid_res_col
    standard+=1

# print(row_max, col_max) # 행에서 가장 큰 값, 열에서 가장 큰 값

to_right=0

for k in range(N):
    to_right+=res[k][k]

to_left=0

for m in range(N):
    to_left+=res[m][N-1-m]


print(max(row_max, col_max, to_left, to_right))