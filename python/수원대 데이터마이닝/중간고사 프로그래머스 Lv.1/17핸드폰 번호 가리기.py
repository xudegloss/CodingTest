## 길이와 인덱싱 이용하기.

print("01033334444"[-4:])
print(len("01033334444")-len("01033334444"[-4:]))

def solution(phone_number):
    number=phone_number[-4:]
    count=len(phone_number)-len(phone_number[-4:])
    return "*"*count+number