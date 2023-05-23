import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path+"//python//코딩테스트 강의 내용//01코드 구현력//"+"input.txt")

N, K = map(int, input().split())
arr=list(map(int, input().split()))

new_list=[]

for i in range(0, N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            new_list.append(arr[i]+arr[j]+arr[z])

new_list=list(set(new_list))
new_list.sort(reverse=True)
print(new_list[K-1])


"""
## 중복을 제거하기 : 집합 이용하기
res=set()
for i in range(0, N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(arr[i]+arr[j]+arr[m]) # set은 append 대신에 add 이용하기

res=list(res)
res.sort(reverse=True)
print(res[K-1])
"""