arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMin=float("inf") # 가장 큰 값으로 초기화 시키기.

for i in range(0, len(arr)):
    if arr[i]<arrMin: # arrMin 보다 작은 경우에 arrMin 업데이트 하기.
        arrMin=arr[i]

print(arrMin)