import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "//python//코딩테스트 강의 내용//01 코드 구현력//" + "input.txt")

N=int(input())
answer=-2147000000

for _ in range(0, N):
    i,j,k = map(int, input().split())
    if i==j==k and answer<10000+i*1000:
        answer=10000+i*1000
    elif i!=j!=k and answer<max(i,j,k)*100:
        answer=max(i,j,k)*100
    elif i==j!=k and answer<1000+100*i:
        answer=1000+100*i
    elif i!=j==k and answer<1000+100*j:
        answer=1000+100*j
    elif i==k!=j and answer<1000+100*i:
        answer=1000+100*i

print(answer)

"""
res=0

for i in range(N):
    tmp=input().split()
    tmp.sort() # 오름차순 정렬하기.
    a, b, c = map(int, tmp)

    ## 3개가 같은 경우 먼저 고려해야 한다. ##
    ## 가장 좋은 조건을 가장 위에 걸어준다. ##

    if a==b and b==c:
        money=10000+1000*a
    elif a==b or a==c:
        money=1000+100*a
    elif b==c:
        money=1000+100*b
    else: # 3개 모두 다른 경우
        money=c*100

    ## 가장 큰 상금을 찾는 코드
    if money>res:
        res=money

print(res)
"""