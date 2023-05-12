import sys
import os

current__path=os.getcwd()
sys.stdin=open(current__path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N=int(input())
math_score=list(map(int, input().split()))
math_avg=round(sum(math_score)/N)
min= 2147000000

for idx, score in enumerate(math_score):
    minus=abs(math_avg-score)
    if minus<min:
        min=minus
        result_score=score
        result_order=idx+1
    elif minus==min: # 가까운 점수가 여러 개 있는 경우
        # 가까운 점수가 여러 개 : 점수가 가장 높은 학생 번호
        # 높은 점수가 여러 개 : 학생 번호가 가장 빠른 학생 번호
        if result_score<score:
            result_score=score
            result_order=idx+1

print(math_avg, result_order)