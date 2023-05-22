import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

iter=10
card_array=[i for i in range(1, 21)]

for _ in range(iter):
    a,b=map(int, input().split())
    card_array = card_array[:a-1] + card_array[a-1 : b][::-1] + card_array[b: ]

print(" ".join(map(str, card_array))) # 문자열인 경우에만 join이 가능하다.

### 변경하는 방법 ### 

# a, b=map(int, input().split())
# a, b = b, a


### 내가 풀이한 코드 ###

"""

a=list(range(1, 21))

for _ in range(10): # 변수 없음
    s, e = map(int, input().split())

    for _ in range((e-s+1)//2): # 1 더해주는 것 까먹지 않기.
        a[s-1], a[e-1] = a[e-1], a[s-1] # swap
        s+=1
        e-=1

print(" ".join(map(str, a)))

"""

### 강사님 풀이한 코드 ###