import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N=int(input())
answer_arr=[0]*(N+1)

for num in range(2, len(answer_arr)):
    for n in range(num*2, len(answer_arr), num):
        answer_arr[n]+=1

    
answer=0
for i in answer_arr[2:]:
    if i==0:
        answer+=1

print(answer)