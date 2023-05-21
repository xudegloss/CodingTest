import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N=int(input())

res=-21470000000 # 최대값을 찾고자 설정한 값

for _ in range(N):

    ### 오름차순 정렬을 진행해야 한다. ###
    ### 그래야 나중에 가장 큰 눈을 찾을 수 있기 때문이다. ###
    tmp=list(map(int, input().split()))
    tmp.sort()
    a, b, c=tmp
    
    if a==b==c:
        price=10000+1000*a
    elif a==b or a==c:
        price=1000+100*a
    elif b==c:
        price=1000+100*b
    else:
        price=100*c

    ## 최대 상금을 찾는 방법
    if res < price:
        res=price

print(res)

### 오름차순 정렬 대신에 max 이용하여 구할 수도 있다. ###

"""

N=int(input())

res=-21470000000 # 최대값을 찾고자 설정한 값

for _ in range(N):

    a,b,c=map(int, input().split())
    
    if a==b==c:
        price=10000+1000*a
    elif a==b or a==c:
        price=1000+100*a
    elif b==c:
        price=1000+100*b
    else:
        price=100*max(a, b, c)

    ## 최대 상금을 찾는 방법
    if res < price:
        res=price

print(res)

"""