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

## 잘 돌아간다... 

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

## 에라토스테네스 체를 이용하여 구하면 제대로 돌아간다.
# 1. 1을 제거한다.
# 2. 2을 선택하고, 2의 배수를 모두 제거한다.
# 3. 3을 선택하고, 3의 배수를 모두 제거한다.
# 4. 반복...

## 시간 초과...
 
def solution(n):
    _list=[]
    for num in range(2, n+1):
        _list.append(num)

    m=int(n**0.5)
    for i in range(2, m+1):
        for j in range(2*i, n+1, i):
            if j in _list:
                _list.remove(j)
    return len(_list)

## chat GPT가 최적화해줌...

def solution(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            primes[i*i:n+1:i] = [False] * len(primes[i*i:n+1:i])

    return sum(primes)