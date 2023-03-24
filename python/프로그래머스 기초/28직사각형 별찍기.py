a, b = map(int, input().strip().split(' '))
# 구글링을 통하여 찾아내었다. a만큼 별 반복하고 개행 진행한 뒤에 그 전체 과정을 b만큼 반복하기.
answer=("*"*a+'\n')*b
print(answer)