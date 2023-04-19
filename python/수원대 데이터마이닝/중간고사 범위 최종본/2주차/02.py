from io import StringIO

## 입력 문자열
input_str = \
"""
25 2
"""

## 문자열을 스트림으로 바꾸는 방법
stream = StringIO(input_str.strip())
input = stream.readline #import sys

## 아래에 코드 작성
n, k = map(int, input().split()) # 25 2

def solution(n, k):
    cnt=0 # 지역 변수로 cnt를 함수 안에 적어줘야 한다. 
    while True:
        if n==1:
            return cnt
        
        if n%k==0:
            n=n//k
            cnt+=1
        else:
            n-=1
            cnt+=1
    pass

print(solution(n, k))
print(solution(17, 4))
print(solution(25, 3))