def solution(arr):
    b = []
    for i in range(len(arr)):
        if i == 0:
            b.append(arr[i])
        elif arr[i] != arr[i-1]:
            b.append(arr[i])

    return b

print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))