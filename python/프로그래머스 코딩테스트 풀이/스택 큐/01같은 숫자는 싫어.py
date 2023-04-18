# 1. stack 구조
# 2. stack 안에 있는 경우 앞의 숫자와 들어올 숫자 비교한다. 같은 경우 제거.
# 3. 다른 경우 뒤에 넣어주기.

def solution(arr):
    stack = []  
    for num in arr:
        # 스택이 비어있지 않고, 끝 숫자와 들어오는 숫자가 같은 경우, 제거한다.
        if stack and stack[-1]==num:
            stack.pop()
        # 그렇지 않는 경우에는 뒤에 붙여준다.
        stack.append(num)
    return stack

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
