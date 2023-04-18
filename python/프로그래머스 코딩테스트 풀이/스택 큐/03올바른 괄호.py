def solution(s):
    stack=[]
    for idx in range(0, len(s)):
        stack.append(s[idx])
        if len(stack)>=2 and stack[-1]==")":
            if stack[-2]=="(":
                stack.pop()
                stack.pop()
    if stack:
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
