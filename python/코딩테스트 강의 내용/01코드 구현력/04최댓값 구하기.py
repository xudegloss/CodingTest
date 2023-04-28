arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMax=float("-inf") # 가장 작은 값으로 초기화 시키기.

for i in range(0, len(arr)):
    if arr[i]>arrMax: # 더 큰 수가 나오면 업데이트 진행하기.
        arrMax=arr[i]

print(arrMax)