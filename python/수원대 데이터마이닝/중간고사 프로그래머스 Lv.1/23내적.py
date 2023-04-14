def solution(a, b):
    return sum([a[idx]*b[idx] for idx in range(0, len(a))])

## 이렇게 풀어도 되지만, zip을 이용하면 더 빠르게 풀 수 있다.