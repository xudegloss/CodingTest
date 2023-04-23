N=5
arr=[2, 3, 1, 2, 2]
arr.sort()

idx=0
new_idx=0
cnt=0

while new_idx<len(arr):
    new_idx+=arr[idx]
    new_list=arr[idx: new_idx]
    if max(new_list)==arr[idx]:
        cnt+=1
    else:
        continue
    idx=new_idx

print(cnt)