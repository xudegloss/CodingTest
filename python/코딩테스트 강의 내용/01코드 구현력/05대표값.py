import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path+"//python//코딩테스트 강의 내용//01코드 구현력//"+"input.txt")

N=int(input())
math_scores=list(map(int, input().split()))
mean_score=round(sum(math_scores)/N, 0)

## idx, value : dictionary 형태로 담아주기.
result={"idx": 0, "value": math_scores[0]}
for i in range(1, N):
    if abs(result["value"]-mean_score) > abs(math_scores[i]-mean_score):
        result["value"]=math_scores[i]
        result["idx"]=i
    elif abs(result["value"]-mean_score) == abs(math_scores[i]-mean_score):
        if math_scores[i] > result["value"]:
            result["value"]=math_scores[i]
            result["idx"]=i
        elif math_scores[i] == result["value"]:
            continue

print(int(mean_score), result["idx"]+1)

"""
min=2147000000 # 2147 + 0 6개
ave=round(sum(math_scores) / N)
for idx, x in enumerate(math_scores):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
        ## 값이 같아도 위의 조건을 만족하지 못 하기 때문에, 그냥 무시하고 돌아간다.
            
print(ave, res)
"""