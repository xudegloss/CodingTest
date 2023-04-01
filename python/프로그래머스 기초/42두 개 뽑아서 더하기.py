# numbers=[5,0,2,7]
# new_numbers=[]

# for i in range(0, len(numbers)):
#     for j in range(i+1, len(numbers)):
#         new_numbers.append(numbers[i]+numbers[j])

# print(sorted(list(set(new_numbers))))

def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))