from collections import deque

def solution(priorities, location):
    # 문서들을 큐에 넣기
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    cnt = 0  # 출력한 문서의 개수

    while queue:
        cur = queue.popleft()
        # 현재 문서보다 중요도가 높은 문서가 있다면 다시 큐에 넣음
        if queue and max(queue)[0] > cur[0]:
            queue.append(cur)
        else:
            cnt += 1
            if cur[1] == location:
                return cnt
            
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
