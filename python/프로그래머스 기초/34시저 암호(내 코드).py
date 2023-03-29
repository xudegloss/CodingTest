# s="a B z"
# s=list(s)
# print(s)

# for idx in range(0, len(s)):
#     if s[idx].isupper(): # 대문자인 경우
#         s[idx]=chr((ord(s[idx])+4-90-1)%26+65)
#         print(s[idx])
#     elif s[idx].islower(): # 소문자인 경우
#         s[idx]=chr((ord(s[idx])+4-122-1)%26+97)

# print("".join(s))

def solution(s, n):
    s=list(s)
    for idx in range(0, len(s)):
        if s[idx].isupper():
            s[idx]=chr((ord(s[idx])+n-90-1)%26+65)
        elif s[idx].islower():
            s[idx]=chr((ord(s[idx])+n-122-1)%26+97)
    return "".join(s)

print(solution("AB", 1))