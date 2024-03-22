def solution(numbers):
    # n : 비교하고자 하는 숫자
    result=0
    for n in range(10):
        if n not in numbers:
            result+=n
    return result