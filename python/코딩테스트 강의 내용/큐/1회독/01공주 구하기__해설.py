from collections import deque

def solution(n, k):
    dq=list(range(1, n+1))
    dq=deque(dq) # deque 자료 구조가 됨.
    
    while dq:
        for _ in range(k-1):
            cur=dq.popleft()
            dq.append(cur)
        dq.popleft()
        
        if len(dq)==1:
            return dq[0]

print(solution(8, 3))