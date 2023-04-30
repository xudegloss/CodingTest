# 1. ( 이면 무조건 stack에 넣어주기.
# 2. ) 나오면 바로 앞이 ( 인지 확인하기. 맞다면 레이저이고, len 만큼 더해주기.
# 3. 아니라면 쇠막대기의 끝이고 제거 후 1만큼 더해주기.

def solution(s):
    s=list(s)
    count=0
    stack=[]

    # idx를 이용하지 않으면 )) 경우를 체크할 수 없게 된다. 그래서 idx 이용하여 체크하기.
    for idx in range(0, len(s)):
        if s[idx]=="(":
            stack.append(s[idx])
        else: # ")"인 경우
            if s[idx-1]=="(":
                stack.pop()
                count+=len(stack)
            else:
                stack.pop() # 나중에 들어온 막대기 먼저 없애주기.
                count+=1
    return count 

print(solution("()(((()())(())()))(())"))
print(solution("(((()(()()))(())()))(()())")) # 왜 26이 나오지?