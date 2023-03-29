arr=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

max_width=max([r[0] for r in arr])
max_height=max([r[1] for r in arr])
arr_size=[]
arr_size.append(max_width*max_height)

arr=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
arr_copy_width=arr.copy()

for i, val in enumerate(arr_copy_width):
    if val[0]==max_width:
        val[0], val[1]=val[1], val[0]

arr_size.append(max(r[0] for r in arr_copy_width)*max(r[1] for r in arr_copy_width))

arr=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]] # 왜 이 부분을 다시 적어야할까?
arr_copy_height=arr.copy()

for i, val in enumerate(arr_copy_height):
    if val[1]==max_height:
        val[0], val[1]=val[1], val[0]

arr_size.append(max(r[0] for r in arr_copy_height)*max(r[1] for r in arr_copy_height))

print(arr_size)