import sys
import os

current__path=os.getcwd()
sys.stdin=open(current__path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

test__case=int(input())

for iter in range(test__case):
    N, s, e, k=map(int, input().split())
    N__arr=list(map(int, input().split()))
    
    new__arr=N__arr[s-1: e]
    new__arr.sort()
    print(f"#{iter+1} {new__arr[k-1]}")