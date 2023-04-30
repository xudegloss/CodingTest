import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "//python//코딩테스트 강의 내용//01 코드 구현력//" + "input.txt")

N=int(input())
array=list(map(int, input().split()))

def digit_sum(arr):
    max=-2174000000
    for num in arr:
        for idx in range(0, len(str(num))):
            print(str(num)[idx])

print(digit_sum(array))