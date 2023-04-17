def solution(s):
    cnt=0
    stack=[]

    for i in range(len(s)):
        if s[i]=="(":
            stack.append(s[i])
        else:
            stack.pop()
            if s[i-1]=="(":
                # stack.pop()
                cnt+=len(stack)
            else:
                # 막대기가 끝나기 때문에 지워야 한다.
                # stack.pop()
                cnt+=1
    return cnt
    

print(solution("()(((()())(())()))(())"))
print(solution("(((()(()()))(())()))(()())")) 