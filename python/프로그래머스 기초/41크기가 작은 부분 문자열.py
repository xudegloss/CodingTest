# 1. t에서 p길이 문자열을 찾기.
# 2. p길이의 문자열을 p의 값과 비교하여 작거나 같은 경우 카운트 넣기.

# t="10203"
# p="15" # len(p)
# idx=0
# result=0

# while True:
#     new_t=t[idx: idx+len(p)]
#     if int(new_t)<=int(p):
#         result+=1
#     if idx+len(p)==len(t):
#         break
#     idx+=1

# print(result)

def solution(t, p):
    answer = 0
    idx=0
    
    while True:
        new_t=t[idx:idx+len(p)]
        if int(new_t)<=int(p):
            answer+=1
        if idx+len(p)==len(t):
            break
        idx+=1
    return answer