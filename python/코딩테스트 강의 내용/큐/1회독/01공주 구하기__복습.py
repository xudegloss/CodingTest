# FIFO : 큐 구조
from collections import deque

def solution(n, k):
    dq=[num for num in range(1, n+1)]
    dq=deque(dq)
    
    # 1. dq의 길이가 1보다 큰 경우에 반복한다.
    while len(dq)>1:

        # 2. (k-1)번 반복하기. (popleft와 append)
        for _ in range(k-1):
            cur=dq.popleft()
            dq.append(cur)

        # 3. k번째는 제거하기. 
        dq.popleft()
        
    return dq[0]

print(solution(8, 3))