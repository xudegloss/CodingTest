## 시간 초과 방지 ##
import sys
input=sys.stdin.readline

N=int(input())
stack=[]

for _ in range(0, N):
    s=input()

    if "push" in s:
        stack.append(int(s.split(" ")[-1]))
    elif "pop" in s:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif "size" in s:
        print(len(stack))
    elif "empty" in s:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else: # top
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])