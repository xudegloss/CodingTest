s=input()
stack=[s[0]] # 일단 한 개를 안에 넣어주기.

for idx in range(1, len(s)):
    if s[idx]=="{" or s[idx]=="[" or s[idx]=="(":
        stack.append(s[idx])
    else:
        if s[idx]=="}" and stack[-1]=="{":
            stack.pop()
        elif s[idx]=="]" and stack[-1]=="[":
            stack.pop()
        elif s[idx]==")" and stack[-1]=="(":
            stack.pop()
            
if len(stack)==0:
    print(True)
else:
    print(False)