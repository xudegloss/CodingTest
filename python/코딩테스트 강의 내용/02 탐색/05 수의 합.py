import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\python\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

n, m=map(int, input().split())
a=list(map(int, input().split()))

lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot<m:
       if rt<n:
           tot+=a[rt]
           rt+=1
       else: # rt == n인 경우 (더하라고는 하는데 더할 값이 없다.)
           break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(cnt)

"""

### Time Limit Exceeded ###

res=0

for i in range(N):
    mid_res=A[i]
    for j in range(i+1, N):
        # M과 동일한 경우
        if mid_res==M:
            res+=1
            break

        # M과 동일하지 않는 경우
        else:
            if mid_res < M:
                mid_res += A[j]
                if mid_res==M:
                    res+=1
                    break
            elif mid_res == M:
                res+=1
                break
            else:
                break
    
print(res)

"""