# 1. 뒤에 들어오는 숫자보다 앞의 숫자가 작으면 앞 제거하기. (스택 비어있음 안 되고, 제거 개수가 남아 있어야 한다.)
# 2. 제거 개수 맞추면 그대로 끝내기.
# 3. 만약에 제거 개수 다 맞춰지지 않는 경우에는 남은 개수 만큼 뒤 자르기.

def solution(n, m):
    n=str(n)
    n=list(map(int, n))
    stack=[]

    for num in n:
        # 왜 제거하는 부분 while 사용했을까?
        # 제거하는 횟수를 내가 지정하는 것이 아니라서...!
        while m>0 and stack and stack[-1]<num:
            stack.pop()
            m-=1
        stack.append(num)
    
    if m!=0:
        return "".join(map(str, stack))[:-m]
    return "".join(map(str, stack))
  
print(solution(5276823, 3))
print(solution(9977252641, 5))