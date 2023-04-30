# 1. ( 나오면 그냥 스택에 넣어주기.
# 2. ) 가 나오면 s의 바로 앞을 봐준다. ( 가 나오면 레이저, ) 가 나오면 스택의 마지막이다.
# 3. 레이저가 나오면 스택을 pop 처리하고, 길이 만큼 더해준다.
# 4. 쇠막대기가 나오면 스택을 pop 처리하고, 1 만큼 더해준다.

def solution(s):
    stack=[]
    result=0

    for idx in range(0, len(s)):

        # 1. ( 나오면 그냥 스택에 넣어주기.
        if s[idx]=="(":
            stack.append(s[idx])

        # 2. ) 가 나오면 s의 바로 앞을 봐준다. ( 가 나오면 레이저, ) 가 나오면 스택의 마지막이다.
        else: # s[idx]==")"

            # 3. 레이저가 나오면 스택을 pop 처리하고, 길이 만큼 더해준다.
            if s[idx-1]=="(":
                stack.pop()
                result+=len(stack)
                
            # 4. 쇠막대기가 나오면 스택을 pop 처리하고, 1 만큼 더해준다.
            else:
                stack.pop()
                result+=1
    return result

print(solution("()(((()())(())()))(())")) # 17
print(solution("(((()(()()))(())()))(()())")) # 24