## 이런 경우에는 count 이용할 수 없다.
## len를 이용하여 짝수인지 홀수인지 판단한다.

def solution(left, right):
    answer=0
    for num in range(left, right+1):
        divisor_count=len([n for n in range(1, num+1) if num%n==0])
        if divisor_count%2==0:
            answer+=num
        else:
            answer-=num
    return answer