# zip + 리스트 컴프리헨션의 이용하기.
# 2개 이상의 순회 가능한 객체를 인자로 받아서 보여준다.
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])