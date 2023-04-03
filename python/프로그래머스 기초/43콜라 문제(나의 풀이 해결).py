def solution(a, b, n):
    answer = 0
    vacant_bottle=0

    while True:
        if n<a:
            break
        # 케이스 나누지 않고 돌리면 제대로 돌아간다.
        # 케이스를 나누면 에러가 뜬다. 왜 그럴까?
        else:
            answer+=(n//a)*b
            vacant_bottle=(n%a)
            n=(n//a)*b                                 
            n+=vacant_bottle
    return answer

print(solution(3, 1, 20))