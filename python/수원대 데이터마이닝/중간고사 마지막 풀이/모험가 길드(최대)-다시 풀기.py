N=int(input())
arr=list(map(int, input().split()))
arr.sort()

idx=0 # 기존 인덱스
new_idx=0 # 새로운 인덱스
cnt=0

while True:
    new_idx+=int(arr[idx])
    if new_idx>=len(arr):
        break
    new_list=arr[idx: new_idx] # 다른 변수로 받아주기.
    if arr[idx]==max(new_list):
        cnt+=1
    else:
        continue
    idx=new_idx # 인덱스 갱신하기.

print(cnt)
