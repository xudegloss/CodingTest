N=int(input())
arr=input().split()
arr.sort(reverse=True)

idx=0
cnt=0

while idx<len(arr):
    idx+=int(arr[idx])
    cnt+=1

print(cnt)
    