import sys
import os

current__path=os.getcwd()
sys.stdin=open(current__path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N, K=map(int, input().split())
arr=list(map(int, input().split()))

new__arr=[]

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            _sum=arr[i]+arr[j]+arr[k]
            new__arr.append(_sum)

new__arr=list(set(new__arr))
new__arr.sort(reverse=True)

print(new__arr[K-1])