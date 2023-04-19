import sys
from collections import deque

N=int(sys.stdin.readline())
dq=[i for i in range(1, N+1)]
dq=deque(dq)

while dq:
    # 조건문을 위에 적어주기.
    if len(dq)==1:
        print(dq[0])
        break
    dq.popleft()
    cur=dq.popleft()
    dq.append(cur)