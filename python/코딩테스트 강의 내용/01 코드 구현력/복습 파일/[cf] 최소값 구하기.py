arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMin=2147000000

for num in arr:
    if num < arrMin:
        arrMin=num

print(arrMin)