def remove_dups(s):
    stack=[]
    for idx in range(0, len(s)):
        if len(stack)<2: 
            stack.append(s[idx])
        else: # stack 길이가 2이상인 경우
            if s[idx]==stack[-1]==stack[-2]:
                stack.pop()
                stack.pop()
            else:
                stack.append(s[idx])
    return "".join(map(str, stack))
    pass
    

print(remove_dups("caaa"))
print(remove_dups("accab"))
print(remove_dups("baccaaac"))