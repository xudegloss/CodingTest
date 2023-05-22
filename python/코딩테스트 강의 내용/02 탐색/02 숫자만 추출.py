import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

# 1. 숫자만 추출하는 함수 만들기.

strs=input()

def pick_number(strs):
    result=[]    
    for s in strs:
        if s.isdigit():
            result.append(s)
    return int("".join(result))

# 2. 약수의 개수 찾는 함수 만들기.

def count_ms(res):
    cnt=0
    for n in range(1, res+1):
        if res%n==0:
            cnt+=1
    return cnt

# 3. 출력 형식에 맞게 출력하기.

print(pick_number(strs))
print(count_ms(pick_number(strs)))

"""

s=input()

res=0
for x in s:
    if x.isdecimal():
        res=res*10+int(x) # 이 식을 이해하기!

print(res)

cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1

print(cnt)

"""