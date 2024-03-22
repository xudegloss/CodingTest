# 제곱 → 제곱근으로 고려해도 괜찮음
# 1보다 작은 수가 등장하는 경우, -1 리턴


## 1 ##
# math 라이브러리 불러오기.
import math

def solution(n):
    # 0이하 조건 必
    if n<=0:
        return -1
    elif int(math.sqrt(n)) == math.sqrt(n):
        # 정수 처리해도 동일해야 한다.
        return int((math.sqrt(n)+1)**2)
    return -1

## 2 ##
# isdigit 함수로 풀이 가능해보임
