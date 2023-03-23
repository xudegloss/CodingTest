# 중복되는 값을 제거하는 경우에 집합 사용한다.
# a=[3,1,6,3,7,7,1]
# result=[i for i in a if i not in {1}]
# print(result)

# 최솟값 구하는 min 함수 이용하기.
def solution(arr):
    answer = []
    if len(arr)==1:
        return [-1]
    else:
        # 꼭 집합으로 만들어주기.
        min_num={min(arr)}
        answer=[i for i in arr if i not in min_num]
        return answer

print(solution([3,1,6,3,7,7,1]))