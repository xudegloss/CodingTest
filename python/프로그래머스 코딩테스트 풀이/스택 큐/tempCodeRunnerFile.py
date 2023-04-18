from collections import deque

def solution(priorities, location):
    # idx : location, val : 값 한꺼번에 표현하기.
    dq=deque((idx, val) for idx, val in enumerate(priorities))
    print(max(dq[:][1]))
    # while dq:
    #     if dq[0][1]<max(dq[1])

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
