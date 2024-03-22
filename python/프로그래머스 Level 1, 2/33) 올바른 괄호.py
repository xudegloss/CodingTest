# "("가 오면 반드시 ")"

def solution(s):
    stack=[]
    for string in s:
        stack.append(string)
        if len(stack)>=2:
            if "".join(stack[len(stack)-2:len(stack)]) == "()":
                stack.pop()
                stack.pop()
                
    if len(stack)==0:
        return True
    return False

    """
    
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
    
    """