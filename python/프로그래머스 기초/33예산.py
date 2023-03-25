###### 문제 잘 읽기! 풀이 방법이 다르다! #####
# def solution(d, budget):
#     answer = 1
#     d.sort()
#     expectation=d[0]

#     for arr in d[1:]:
#         if expectation<budget:
#             expectation+=arr
#             if expectation<=budget:
#                 answer+=1
#             else:
#                 break
#     return answer

# print(solution([1,3,2,5,4], 9))
# print(solution([2,2,3,3], 10))

# d=[2,2,3,3]	
# budget=10
# expectation=d[0]
# result=1

# for arr in d[1:]:
#     if expectation<budget:
#         expectation+=arr
#         print(arr, expectation)
#         if expectation<=budget:
#             result+=1
#         else:
#             break
#     else:
#         break

# print(result)

def solution(d, budget):
    d.sort()
    total_sum=sum(d) # 총 합
    total_count=len(d) # 총 개수
    for _max in d[::-1]:
        if total_sum>budget:
            total_sum-=_max
            total_count-=1
        else:
            break
    return total_count

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))
