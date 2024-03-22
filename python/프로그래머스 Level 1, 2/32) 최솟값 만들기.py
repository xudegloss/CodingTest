# A => 오름차순 정렬
# B => 내림차순 정렬

def solution(A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    result = 0
    
    for idx in range(0, len(A)):
        result+=(A[idx] * B[idx])
    return result