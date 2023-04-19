def solution(numbers):
    return sum([num for num in range(0, 10) if num not in numbers])

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))