# 1. 열린 괄호가 나오면 스택에 그냥 붙여주기.
# 2. 닫힌 괄호가 나오면 바로 앞 열린 괄호이면 스택 가장 위 제거 후 길이 만큼 더해주기.
# 3. 그게 아니라면 제거 후 +1 처리하기.

def solution(s):
    answer=0
    stack=[]

    for idx in range(0, len(s)):
        if s[idx]=="(":
            stack.append(s[idx])
        else:
            if s[idx-1]=="(":
                stack.pop()
                answer+=len(stack)
            else:
                stack.pop()
                answer+=1
    return answer

print(solution("((()()))")) # 6
print(solution("()(((()())(())()))(())")) # 17
