from collections import deque

def solution(priorities, location):
    # idx : location, val : 값 한꺼번에 표현하기.
    dq=deque((val, idx) for idx, val in enumerate(priorities))
    answer_dq=deque()    
    
    iter=0
    while dq:
        for _ in range(iter, len(dq)):
            if dq[iter][0] < max(dq)[0]:
                cur=dq[iter]
                dq.remove(cur)
                dq.append(cur)
        answer_dq.append(dq[iter])
        iter+=1
        if iter==len(dq):
            break
    
    for _ in range(0, len(answer_dq)):
        if answer_dq[_][1]==location:
            return _+1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
