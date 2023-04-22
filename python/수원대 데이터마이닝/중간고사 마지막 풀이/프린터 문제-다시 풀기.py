from collections import deque

def solution(priorities, location):
    # 문서들을 큐에 넣기
    queue = deque([(val, idx) for idx, val in enumerate(priorities)])
    cnt = 0  # 몇 번째로 출력하는지 카운트하기.
    
    while queue:
        cur=queue.popleft()
        if queue and cur[0]<max(queue)[0]:
            queue.append(cur)
        else:
            cnt+=1
            if cur[1]==location:
                return cnt

print(solution([2, 1, 3, 2], 2))
print(solution([2, 1, 3, 2], 1))
print(solution([2, 1, 3, 2], 3))
print(solution([1, 1, 9, 1, 1, 1], 0))