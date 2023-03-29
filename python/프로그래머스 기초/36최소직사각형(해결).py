# arr=[[60, 50], [30, 70], [60, 30], [80, 40]]
# large_arr=[]
# small_arr=[]

# for iter in range(0, len(arr)):
#     if arr[iter][0]>=arr[iter][1]:
#         large_arr.append(arr[iter][0])
#         small_arr.append(arr[iter][1])
#     else:
#         large_arr.append(arr[iter][1])
#         small_arr.append(arr[iter][0])

# print(large_arr)
# print(small_arr)
# print(max(large_arr)*max(small_arr))

def solution(sizes):
    answer=0
    large_arr=[]
    small_arr=[]
    
    for iter in range(0, len(sizes)):
        if sizes[iter][0]>=sizes[iter][1]:
            large_arr.append(sizes[iter][0])
            small_arr.append(sizes[iter][1])
        else:
            large_arr.append(sizes[iter][1])
            small_arr.append(sizes[iter][0])

    answer=max(large_arr)*max(small_arr)
    return answer