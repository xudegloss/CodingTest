def solution(food):
    answer=[]
    for idx in range(1, len(food)):
        answer.append(str(idx)*(food[idx]//2))
    return "".join(map(str, answer+[0]+answer[::-1]))

# 아래는 수정하지 마시오.
print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))