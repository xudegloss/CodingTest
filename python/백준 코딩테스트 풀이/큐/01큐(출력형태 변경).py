## 시간 초과 방지 ##
import sys
input=sys.stdin.readline

from collections import deque

## 자꾸 줄바꿈이 생겨서 출력 형태가 달라진다.

N=int(input())
dq=deque()

for iter in range(0, N):
    a=input()

    if "push" in a:
        dq.append(a.split(" ")[1])
    elif "size" in a:
        print(len(dq))
    elif "empty" in a:
        if len(dq)==0:
            print(1)
        else:
            print(0)
    else:
        if len(dq)==0:
            print(-1)
        else:
            # end=""은 줄바꿈 일어나지 않게 출력한다. 
            if "pop" in a:
                print(dq.popleft(), end="")
            elif "front" in a:
                print(dq[0], end="")
            else:
                print(dq[-1], end="")