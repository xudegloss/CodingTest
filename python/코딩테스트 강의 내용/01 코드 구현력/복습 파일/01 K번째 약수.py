import sys
import os

current__path=os.getcwd()
sys.stdin=open(current__path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")
# open(file, mode)

N, K=map(int, input().split())

# cnt : 약수의 순서
# i : 약수인지 아닌지 판별하는 수

cnt=0

for i in range(1, N+1):
    if N%i==0:
        cnt+=1
        if cnt==K:
            print(i)
            break

else:
    print(-1)

### while을 이용하여 풀이한 방법 ###

# cnt=0
# i=1

# while i<=N:
#     if N%i==0:
#         cnt+=1
#         if cnt==K:
#             print(i)
#             break
#     i+=1

# else:
#     print(-1)