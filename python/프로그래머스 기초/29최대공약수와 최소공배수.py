def solution(n, m):
    answer = []
    
    # 최대 공약수 구하기
    s1=set([i for i in range(1, n+1) if n%i==0])
    s2=set([i for i in range(1, m+1) if m%i==0])
    answer.append(max(s1.intersection(s2)))
    
    # 최소 공배수 구하기
    if m<n:
        m,n=n,m

    if m%n==0:
        answer.append(m)
        return answer
    else:
        for num in range(1, n*m+1):
            if (num%n==0) and (num%m==0):
                answer.append(num)
                # 한 개가 들어가는 즉시 바로 반복문 종료시키기.
                break
    return answer

# s1=set([i for i in range(1, 3+1) if 3%i==0])
# s2=set([i for i in range(1, 12+1) if 12%i==0])
# # 최대 공약수 구하기
# print(max(s1.intersection(s2)))

# # 최소 공배수 구하기
# if 5%2==0:
#     print(5)
# else:
#     for num in range(5*2+1):
#         if (num%2==0) and (num%5==0):
#             print(num)

print(solution(12, 3))
print(solution(3, 12))
print(solution(2, 5))