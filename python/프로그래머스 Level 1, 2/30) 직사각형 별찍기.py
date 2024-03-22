## map과 list 이용하여 입력받는 방법 ##

a, b = map(int, input().split(' '))

# a = n (별의 개수)
# b = m (반복 횟수)

for i in range(b):
    print("*"*a)