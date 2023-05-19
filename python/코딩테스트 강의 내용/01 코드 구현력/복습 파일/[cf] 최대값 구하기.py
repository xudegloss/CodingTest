arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMax=-2147000000 # 최소값 지정하기.

for num in arr:
    if num > arrMax:
        arrMax=num

print(arrMax)


### idx를 이용하여 최대값을 구할 수 있다.

# for idx in range(0, len(arr)):
#     if arr[idx] > arrMax:
# 위에서 부등호는 문제에 따라 달라진다.
# 같은 숫자 등장 시에 앞이 더 중요하면 포함 안 하는 부등호 이용하기.
#         arrMax=arr[idx]

# print(arrMax)