# n=5
# answer=0

# for num in range(1, n+1):
#     for check in range(2, num+1):
#         if (num%check==0) and (check!=num):
#             break
#         elif (num%check==0) and (check==num):
#             answer+=1
#             continue

# print(answer)

## 시간 초과...

def solution(n):
    answer = 0
    for num in range(1, n+1):
        for check in range(2, num+1):
            if (num%check==0) and (check!=num):
                break
            elif (num%check==0) and (check==num):
                answer+=1
                continue
    return answer

## 시간 초과...

def solution(n):
    count=0
    for n in range(2, n+1):
        for i in range(2, n):
            if n%i==0:
                break
        else:
            count+=1
    return count

## 에라토스테네스 체를 이용하여 구하면 제대로 돌아간다.
# 알바 끝나고 살펴보기.

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)