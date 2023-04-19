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
string_list=[]

for string in s:
    if string.isdigit()==True:
        num+=int(string)
    else:
        string_list.append(string)

print("".join(list(map(str, string_list+[num]))))
