## stack

def solution(arr):
    stack = [arr[0]]
    for idx in range(1, len(arr)):
        stack.append(arr[idx])
        if stack[len(stack)-2]==arr[idx]:
            stack.pop()
    return stack

print(solution([1,1,3,3,0,1,1]))