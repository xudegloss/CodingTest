# 핸드폰 번호 변경하는 방법
# phone="01033334444"
# encoding_phone="*"*len(phone[:-4])+phone[-4:]
# print(encoding_phone)

def solution(phone_number):
    return "*"*len(phone_number[:-4])+phone_number[-4:]