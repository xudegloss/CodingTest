# print(sum(i for i in range(1, 13+1) if 13%i==0))
def solution(left, right):
    answer = 0
    # 약수의 개수가 짝수이면 더하고 약수의 개수가 홀수이면 빼기
    for num in range(left, right+1):
        result=0 # 각 숫자의 약수의 개수
        for i in range(1, num+1):
            if num%i==0:
                result+=1

        if result%2==0: # 약수의 개수가 짝수인 경우
            answer+=num # 숫자를 더하기
        else:
            answer-=num # 숫자를 빼기
    return answer

# answer=0
# for num in range(13, 17+1):
#     result=0
#     for i in range(1, num+1):
#         if num%i==0:
#             result+=1
#     print(result)

#     if result%2==0:
#             answer+=num
#     else:
#             answer-=num
# print(answer)


