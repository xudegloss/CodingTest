# arr=[-2, 3, 0, 2, -5]

# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         for z in range(j+1, len(arr)):
#             print(i, j, z)

def solution(number):
    answer = 0
    for i in range(0, len(number)):
        for j in range(i+1, len(number)):
            for z in range(j+1, len(number)):
                if number[i]+number[j]+number[z]==0:
                    answer+=1
    return answer