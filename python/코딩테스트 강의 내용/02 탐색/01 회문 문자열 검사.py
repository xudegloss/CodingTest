import sys
import os

current_path=os.getcwd() 
sys.stdin=open(current_path+"\\코딩테스트 강의 내용\\02 탐색\\"+"input.txt","rt")

N=int(input())

for idx in range(N):
    word=input().lower() # upper()와 반대되는 개념
    word_reverse=word[::-1]
    
    if word==word_reverse:
        print(f"#{idx+1} YES")
    else:
        print(f"#{idx+1} NO")


## 어떤 코드를 위에 올리느냐에 따라 답이 달라진다. ##

"""

N=int(input())

for idx in range(N):
    word=input().lower() # upper()와 반대되는 개념
    size=len(word)

    ### 하나라도 다른 경우 나오면 NO 출력해야 한다. ###

    for j in range(size//2):
        if word[j]!=word[size-1-j]:
            print(f"#{idx+1} NO")
            break
    else:
        print(f"#{idx+1} YES")

"""
