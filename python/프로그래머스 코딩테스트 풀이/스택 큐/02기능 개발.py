def solution(progresses, speeds):
    answer = []
    stack=[]
    remaining_list=[]

    # 1. 남은 일 수 구하기.
    for idx in range(0, len(progresses)):
        if (100-progresses[idx])%speeds[idx]==0:
            remaining=(100-progresses[idx])//speeds[idx]
            remaining_list.append(remaining)
        else:
            remaining=(100-progresses[idx])//speeds[idx]+1
            remaining_list.append(remaining)

    # 2. 작업 일 수에 따른 기능 개수 구하기.
    for day in remaining_list:
        if stack and stack[0]<day:
            answer.append(len(stack))
            while stack:
                stack.pop()
        stack.append(day)
        print(stack)
    answer.append(len(stack))
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
