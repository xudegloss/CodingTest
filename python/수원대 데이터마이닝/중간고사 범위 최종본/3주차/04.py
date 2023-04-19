## 모든 경우 - 3을 제외한 경우

def solution(n):
    return ((n+1) * 60 * 60) - (n * 45 * 45)

print(solution(5))