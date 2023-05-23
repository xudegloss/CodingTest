import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\python\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

## 내가 구현한 코드 ##

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
c=[]

p1=0
p2=0

while True:
    if p1==n or p2==m:
        if p1==n:
            add_list=b[p2:]
        else:
            add_list=a[p1:]
        break
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

print(" ".join(map(str, c + add_list)))

## 강사님이 구현한 코드 ##

# p1=p2=0

while p1<n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2+=1

if p1<n:
    c=c+a[p1:]
if p2<m:    
    c=c+b[p2:]


for x in c:
    print(x, end=' ') # 옆으로 출력하는 방법

"""

### 파이썬스럽게 풀이하였지만, 직접 구현한 풀이가 아니다. ###

n1=int(input())
arr1=list(map(int, input().split()))
n2=int(input())
arr2=list(map(int, input().split()))

new_arr=arr1+arr2
new_arr.sort()
print(" ".join(map(str, new_arr)))

"""