## sort : 리스트에서만 가능하다.
## sorted : 문자열에서도 가능하다.

def solution(s):
    lower=[s for s in sorted(s) if s==s.lower()][::-1]
    upper=[s for s in sorted(s) if s==s.upper()][::-1]
    return "".join([s for s in lower+upper])

def solution(s):
    s=sorted(s)
    s="".join(s)
    return s[::-1]

## 이렇게 풀어도 알아서 대문자를 가장 뒤에 놔준다.