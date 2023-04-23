T=[73, 74, 75, 71, 69, 72, 76, 73]

result=[]
for i in range(0, len(T)):
    cnt=1
    stack=[T[i]]
    for j in range(i+1, len(T)):
        if stack[0] < T[j]:
            result.append(cnt)
            break
        else:
            cnt+=1
            if j==len(T)-1:
                result.append(0)

result.append(0)
print(result)