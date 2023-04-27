import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path+"//python//코딩테스트 강의 내용//01코드 구현력//"+"input.txt")

T=int(input())

for iter in range(0, T):
    N, s, e, k=list(map(int, input().split( )))
    num_list=list(map(int, input().split( )))
    
    new_list=num_list[s-1: e]
    new_list.sort()
    print(f"#{iter+1} {new_list[k-1]}")
    ## print("#%d %d" %(iter+1, a[k-1]))