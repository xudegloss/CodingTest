# 논리가 썩 좋은 편은 아니다.

def solution(nums):
    pick_num=len(nums)//2
    nums=list(set(nums))
    if len(nums)<pick_num:
        return len(nums)
    else:
        return pick_num

print(solution([3,3,3,2,2,4]))