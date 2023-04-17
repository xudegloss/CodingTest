n, m = map(int, input().split())

def solution(n, m):
    n=list(map(int, str(n))) # 리스트로 변경하기.
    stack=[]

    for num in n:
        # 비어있지 않는 경우 참이다.
        # stack에 비어있지 않다.
        while stack and m>0 and stack[-1]<num:
            stack.pop()
            m-=1
        stack.append(num)
    if m!=0:
        stack=stack[:-m]
    res="".join(map(str, stack))
    return res

print(solution(n, m))