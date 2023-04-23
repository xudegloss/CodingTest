
from collections import deque

def printer_order(priorities, location):
    queue =  deque([(val, idx) for idx, val in enumerate(priorities)])
    answer = 0

    while queue:
        cur=queue.popleft()
        if queue and cur[0] < max(queue)[0]:
            queue.append(cur)
        else:
            answer+=1
            if cur[1]==location:
                return answer

print(printer_order([2, 1, 3, 2], 2))    
print(printer_order([2, 1, 3, 2], 1))
print(printer_order([2, 1, 3, 2], 3))
print(printer_order([1, 1, 9, 1, 1, 1], 0))