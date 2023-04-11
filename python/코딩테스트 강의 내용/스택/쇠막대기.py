# 문제가 이해가 안 감....

def solution(s):

    # 1. 열린 괄호는 무조건 스택에 넣어주기.
    # 2. 닫힌 괄호가 나오면 스택의 마지막 확인하기. 
    # 3. 바로 앞에 열린 괄호 있으면 스택 위의 것 제거하고 스택 길이 만큼 더하기.

    sum=0
    stack=[]

    for idx in range(0, len(s)):
        if s[idx]=='(':
            stack.append(s[idx])
        else:
            stack.pop()
            if s[idx-1]=='(':
                # stack.pop()
                sum+=len(stack)
            else:
                # stack.pop()
                sum+=1
    return sum

print(solution("((()()))")) # 6
print(solution("()(((()())(())()))(())")) # 17