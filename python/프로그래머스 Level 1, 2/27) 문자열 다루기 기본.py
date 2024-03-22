# 문자열 s의 길이가 4 혹은 6, 숫자 구성 -> True 출력
# 나머지 -> False 출력

def solution(s):
    if len(s)==4 and s.isdigit()==True:
        return True
    elif len(s)==6 and s.isdigit()==True:
        return True
    return False