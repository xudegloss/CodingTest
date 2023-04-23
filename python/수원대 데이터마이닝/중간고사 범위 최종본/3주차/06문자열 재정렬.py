from io import StringIO

## 입력 문자열
input_str = \
"""
K1KA5CB
"""

## 문자열을 스트림으로 바꾸는 방법
stream = StringIO(input_str.strip())
input = stream.readline

## 아래에 코드를 작성하시오.

s=list(map(str, input()))
s.sort()
num=0
new_list=[]

for idx in range(0, len(s)):
    if s[idx].isdigit()==True:
        num+=int(s[idx])
    else:
        new_list.append(s[idx])

print("".join(map(str, new_list))+str(num))