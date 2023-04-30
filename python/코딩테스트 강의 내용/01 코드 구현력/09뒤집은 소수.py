import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "//python//코딩테스트 강의 내용//01 코드 구현력//" + "input.txt")

N=int(input())
array=list(map(int, input().split()))

def reverse(x):
    while int(str(x)[-1])==0:
        x=int(str(x)[:-1])
    return int(str(x)[::-1])

"""
## 굳이 str, int 변환을 반복할 필요가 없다.
def reverse(x):
  x = str(x)
  return int(x[::-1])
"""

def isPrime(x):
    ## x가 1인 경우는 그냥 고려하지 않기. 왜냐하면 1은 소수가 될 수 없기 때문이다.
    if x<2:
        return 
    for i in range(2, x):
        if x%i==0:
            return 
    return x

result=[]
for num in array:
    num=reverse(num)
    result.append(isPrime(num))    

# None 제거하는 방법 : filter 이용하기.
result=list(filter(None, result)) # filter(적용시킬 함수, 적용할 요소들)
print(" ".join(map(str, result)))

"""
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1): ## 절반까지 돌기.
        if x%i==0:
            return False ## 함수 종료
    else:
        return True

for x in array:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")
"""