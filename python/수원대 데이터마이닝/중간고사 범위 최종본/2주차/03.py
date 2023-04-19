from io import StringIO

## 입력 문자열
input_str = \
"""
02984
"""

## 문자열을 스트림으로 바꾸는 방법
stream = StringIO(input_str.strip())
input = stream.readline#import sys

## 아래에 코드 작성
s=input()

def solution(s):
    answer=int(s[0])
    for idx in range(0, len(s)-1):
        if (int(s[idx])==0) or (int(s[idx])==1):
            answer+=int(s[idx+1])
        else:
            answer*=int(s[idx+1])
    return answer
    pass

print(solution(s)) # 576
print(solution("567")) # 210