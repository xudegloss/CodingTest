# T=[73, 74, 75, 71, 69, 72, 76, 73]

T=list(map(int, input().split()))
result=[]

idx=0
while idx<len(T):
    stack=[T[idx]]
    for i in range(idx+1, len(T)):
        if stack[0]<T[i]:
            cnt=len(stack)
            result.append(cnt)
            break
        else:
            stack.append(T[i])
            if i==len(T)-1:
                result.append(0)
    idx+=1

result.append(0)
print(result)