# swap + sum 함수 이용하기
def solution(a, b):
    if a>b:
        a,b = b,a
    # print(a,b) 결과는 (3,5) 출력된다.
    return sum(range(a, b+1))

print(solution(5,3))