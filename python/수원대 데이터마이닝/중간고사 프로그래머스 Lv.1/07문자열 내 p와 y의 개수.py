# p,y 없는 경우와 개수가 같은 경우 true
# 그렇지 않는 경우 false

## 개수 세는 경우에는 대 소문자 구분하지 않기 때문에, lower를 이용하여 count해주기.
## 개수 같으면 True를 반환한다.

def solution(s):
    if ("p" not in s) and ("y" not in s):
        return True
    return s.lower().count('p') == s.lower().count('y')