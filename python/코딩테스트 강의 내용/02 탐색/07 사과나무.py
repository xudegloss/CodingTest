import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\python\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

N=int(input())
res=0
arr=[]

for i in range(N):
    arr.append(list(map(int, input().split())))

# 문제 접근 방식 : 나눠서 합하여 전체적으로 더하는 방식으로 풀이할 예정이다.
# 1. top_res
# 2. mid_res
# 3. bottom_res
# 4. tot_res = top_res + mid_res + bottom_res

# 1. top_res

top_res=arr[0][N//2]
iter=1

for i in range(1, N//2):
    for j in range(N//2-iter, (N//2+1)+iter):
        top_res+=arr[i][j]
    iter+=1


# 2. mid_res

mid_res=sum((arr[N//2]))

# 3. bottom_res

bottom_res=0
iter=0

for i in range(N-1, N//2, -1):
    for j in range(N//2-iter, (N//2+1)+iter):
        bottom_res+=arr[i][j]
    iter+=1
    
# 4. tot_res

tot_res=top_res+mid_res+bottom_res
print(tot_res)