print([i for i in range(1, 11) if 10%i==1])
print(min([i for i in range(1, 11) if 10%i==1]))

def solution(n):
    return min(i for i in range(1, n+1) if n%i==1)