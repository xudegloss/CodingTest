N=int(input())

for _ in range(0, N):
    stack=[]
    bracket=input()
    for idx in range(0, len(bracket)):
        if bracket[idx]=="(":
            stack.append(bracket[idx])
        else:
            if stack and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(bracket[idx])

    if stack:
        print("NO")
    else:
        print("YES")
