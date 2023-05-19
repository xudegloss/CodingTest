import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N=int(input())
num_arr=list(map(int, input().split()))

def digit_sum(x):
    result=0
    for _ in range(len(str(x))):
        result+=(x%10)
        x=x//10

    return result

arrMax=-214700000000
answer=0

for idx in range(N):
    if digit_sum(num_arr[idx]) > arrMax:
        arrMax=digit_sum(num_arr[idx])
        answer=num_arr[idx]

print(answer)
