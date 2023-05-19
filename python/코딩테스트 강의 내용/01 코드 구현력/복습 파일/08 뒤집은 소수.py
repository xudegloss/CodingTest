import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "\\python\\코딩테스트 강의 내용\\01 코드 구현력\\복습 파일\\" + "input.txt", "rt")

N=int(input())
arr=list(map(int, input().split()))

def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    ### x가 1인 조건 빼먹지 않고 넣어주기.
    if x==1:
        return False
    
    for divide in range(2, (x//2)+1):
        if x%divide==0:
            return False
    else:
        return True
        

for idx in range(len(arr)):
    reverse_n=reverse(arr[idx])
    
    ### true, false로 반환한 뒤에 조건문 이용하여 출력하기.
     
    if isPrime(reverse_n):
        print(reverse_n, end=" ")
    # print(isPrime(reverse_n), end=" ")