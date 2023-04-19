def check_seven(a, b):
    if round(a+b)==0.9: # 반올림 함수
        # 0.5 기준으로 올릴 것인지 내릴 것인지 판단하기.
        return True
    return False
    pass

# 아래는 수정하지 마시오.
print(check_seven(0.1, 0.8))
print(check_seven(0.2, 0.7))
print(check_seven(0.3, 0.6))
print(check_seven(0.4, 0.5))
