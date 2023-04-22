T=[73, 74, 75, 71, 69, 72, 76, 73]

result=[]
for i in range(0, len(T)):
    stack=[T[i]]
    for j in range(i+1, len(T)):
        if stack[0] < T[j]:
            result.append(len(stack))
            break
        else:
            stack.append(T[j])
            if j==len(T)-1:
                result.append(0)
            continue

result.append(0) # 마지막은 무조건 0이 붙는다.
print(result)