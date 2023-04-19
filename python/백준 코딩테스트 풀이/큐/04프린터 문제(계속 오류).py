import sys
from collections import deque

N=int(sys.stdin.readline())
location=0

for _ in range(0, N):
    ## 2개 한꺼번에 입력받고 싶으면 이렇게 코드짜기.
    length, position = map(int, sys.stdin.readline().split())
    priority=map(int, sys.stdin.readline().split())
    dq=deque([(val, idx) for val, idx in enumerate(priority)])

    while dq:
        cur=dq.popleft()
        if dq and max(dq)[0] > cur[0]:
            dq.append(cur)
        else:
            location+=1
            if cur[1]==position:
                print(location)

