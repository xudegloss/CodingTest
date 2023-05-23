import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "//python//코딩테스트 강의 내용//01 코드 구현력//" + "input.txt")

N=int(input())
array=list(map(int, input().split()))

def digit_sum(arr):
    max=-2174000000 # 최대 합을 찾는 값
    result=0 # 최대 합을 가진 숫자를 찾는 값
    for num in arr:
        cnt=0
        for idx in range(0, len(str(num))):
            cnt+=int(str(num)[idx])
        if cnt > max:
            max=cnt
            result=num
    return result

print(digit_sum(array))

"""
둘 다 알아두는 것이 좋다!

### 1. 몫과 나머지 이용하기. ###
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

max=-2147000000
for x in array:
    tot=digit_sum(x)
    if max < tot:   
        max=tot
        res=x

print(res)

### 2. String 처리하여 각각 더해주기. ###
def digit_sum(x):
    sum=0
    for i in str(x): # 굳이 idx 이용하지 않고도 str 이용하여 각각을 가져올 수 있다.
        sum+=int(i)
    return sum

max=-2147000000
for x in array:
    tot=digit_sum(x)
    if max < tot:   
        max=tot
        res=x

print(res)
"""