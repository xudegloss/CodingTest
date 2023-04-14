def solution(s):
    answer = True
    if len(s)==4 and s.isdigit()==True:
        return answer
    elif len(s)==6 and s.isdigit()==True:
        return answer
    else:
        return not answer

## ~와 not은 다른 결과가 나온다.
## 왜 다른 결과가 나오는지는 잘 모르겠다.

print(~True) # -2
print(not True) # False

print(~False) # -1
print(not False) # True
