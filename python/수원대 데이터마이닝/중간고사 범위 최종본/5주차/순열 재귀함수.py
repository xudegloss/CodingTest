A=[1, 2, 3]
N=len(A)
visited=[0]*N
arr=[0]*N

def permute(level):
    if level>=N:
        print(arr)
        return
    
    for i in range(0, len(A)):
        if visited[i]==1:
            continue
        else:
            visited[i]=1
            arr[level]=A[i]
            permute(level+1)
            visited[i]=0
            arr[level]=0

print(permute(0))