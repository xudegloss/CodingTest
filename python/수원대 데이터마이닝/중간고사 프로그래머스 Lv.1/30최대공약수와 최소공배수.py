def solution(n, m):
    answer = []
    
    # 1. 최대 공약수 구하기
    ms_n=[i for i in range(1, n+1) if n%i==0]
    ms_m=[i for i in range(1, m+1) if m%i==0]

    ms=max([num for num in ms_n if num in ms_m])
    answer.append(ms)
    
    # 2. 최소 공배수 구하기
    i=m
    if n>m:
        i=n
    while i<=n*m:
        if (i%n==0) and (i%m==0):
            answer.append(i)
            break
        i=i+1
    return answer

print(solution(2, 5))
