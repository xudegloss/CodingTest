def solution(n):
    answer = []
    while True:
        if n>=3:
            answer.append(str(n%3)) # 나머지
            n=n//3 # 몫
        else:
            answer.append(str(n%3))
            break
    total_answer="".join(answer)

    result=0
    for idx, num in enumerate(total_answer[::-1]):
        result+=3**int(idx)*int(num)
    return result

print(solution(45))

# num=45
# n=3
# answer=[]
# while True:
#     if num>=n:
#         answer.append(str(num%n))
#         num=num//n
#         if num<=n:
#             answer.append(str(num))
#             break

# print("".join(answer))

# result=0
# for idx, num in enumerate("".join(answer)[::-1]):
#     print(idx, num)
#     result+=n**int(idx)*int(num)
# print(result)