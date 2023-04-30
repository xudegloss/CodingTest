# 1. LIFO : Stack 구조
# 2. 새로 들어오는 숫자가 앞의 숫자보다 큰 경우 앞의 숫자 모두 날려버리기.
# 3. 만약에 제거 개수 모두 충족 시키지 못하면 뒷 부분 날리기.

def solution(n, m):
    stack=[]
    n=list(map(int, str(n)))

    for num in n:
        while stack and m>0 and num>stack[-1]:
            stack.pop()
            m-=1
        stack.append(num)
    
    if m!=0:
        return "".join(map(str, stack[:-m]))
    return stack


print(solution(5276823, 3))
print(solution(9977252641, 5))
