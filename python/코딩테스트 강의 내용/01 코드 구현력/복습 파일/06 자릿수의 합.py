import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N=int(input())
num_arr=list(map(int, input().split()))

def digit_sum(x):
    result=0
 
    for idx in range(0, len(str(x))):
        result+=int(str(x)[idx])

    return result # 각 자리수 더한 합

### 반복문 밖에 넣어줘야 한다.

arrMax=-21470000000
answer=0

for idx in range(N):
    if digit_sum(num_arr[idx])>arrMax:
        arrMax=digit_sum(num_arr[idx])
        answer=num_arr[idx]

print(answer)
