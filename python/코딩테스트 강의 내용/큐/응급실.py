from collections import deque

n,m =5,2
Q=[(pos, val) for pos, val in enumerate([60, 50, 70, 80, 90])]
Q=deque(Q)

cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break

print(cnt)
    