import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\python\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

N=9
arr=[]

# 1. 스토쿠 보드 가져오기.

for i in range(N):
    arr.append(list(map(int, input().split())))

# 2. 네모 박스 안에서 체크해야 한다.

## try 1

res_arr=[]
new_arr=[]

for row in range(0, 3):
    for col in range(0, 3):
        new_arr.append(arr[row][col])

res_arr.append(new_arr)

## try 2

new_arr=[]

for row in range(0, 3):
    for col in range(6, 9):
        new_arr.append(arr[row][col])

res_arr.append(new_arr)

## try 3

new_arr=[]

for row in range(3, 6):
    for col in range(3, 6):
        new_arr.append(arr[row][col])

res_arr.append(new_arr)

## try 4

new_arr=[]

for row in range(6, 9):
    for col in range(0, 3):
        new_arr.append(arr[row][col])

res_arr.append(new_arr)

## try 5

new_arr=[]

for row in range(6, 9):
    for col in range(6, 9):
        new_arr.append(arr[row][col])

res_arr.append(new_arr)


for i in range(5):
    if len(set(res_arr[i]))==N:
        continue
    else:
        print("NO")
        break

else:
    print("YES")

"""

### 문제 잘못 이해함 ###

# 2. 각 행에서 중복 여부 확인하기.

for i in range(N):
    length=len(arr[i])
    if length==len(set(arr[i])):
        continue
    else:
        print("NO")
        break

# 3. 각 열에서 중복 여부 확인하기.

col=0

while col<N:
    new_arr=[]
    for i in range(N):
        new_arr.append(arr[i][col])

    if N==len(set(new_arr)):
        col+=1
        continue
    else:
        print("NO")
        break

"""