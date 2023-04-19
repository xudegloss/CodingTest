def list_product(a, b):
    answer=[]
    for idx in range(0, len(a)):
        answer.append(a[idx]*b[idx])
    return answer
    pass

# 아래는 수정하지 마시오.
print(list_product([1,2,3], [4,5,6]))
print(list_product([2,4,6], [3,6,9]))