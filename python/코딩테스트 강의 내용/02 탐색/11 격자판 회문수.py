import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\python\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")
  
N=7
arr=[]

for i in range(N):
    arr.append(list(map(int, input().split())))

# new_arr는 행 방향 일직선 모두 가져온다.
# 접근하려고 하였으나, 자꾸 삼중 반복문 나와서 성능 안 좋음.
# 어떻게 접근해야 되는지 잘 모르겠음.   