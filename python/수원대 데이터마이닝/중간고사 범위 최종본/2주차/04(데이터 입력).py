from io import StringIO
from collections import deque

## 입력 문자열
input_str = \
"""
5
2 3 1 2 2
"""

## 문자열을 스트림으로 바꾸는 방법
stream = StringIO(input_str.strip())
input = stream.readline#import sys

## 아래에 코드 작성
## 데이터 받아오는 것 잘 기억하기.
n=int(input()) # 5
arr=list(map(int, input().split())) # [2, 3, 1, 2, 2]
arr.sort(reverse=True) # [3, 2, 2, 2, 1]

dq=deque(arr)
cnt=0

while dq:
    iter=dq[0]
    for _ in range(iter):
        dq.popleft()
    cnt+=1

    if len(dq)==0:
        print(cnt)
        break