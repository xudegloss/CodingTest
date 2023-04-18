from collections import deque

def solution(priorities, location):
    # idx : location, val : 값 한꺼번에 표현하기.
    dq=deque((val, idx) for idx, val in enumerate(priorities))

    for _ in range(0, len(dq)):
        if dq[0][0]<max(dq)[0]:
            remove_val=dq.popleft()
            dq.append(remove_val)
    
    for i in range(0, len(dq)):
        if dq[i][1]==location:
            return i+1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
