string="23four5six7"
isDigit=[]

for str in string:
    if str.isdigit()==True:
        isDigit.append(True)
    else:
        isDigit.append(False)

isState=isDigit[0]
answer=[]
mid_idx=0

for idx in range(0, len(string)):
    if isDigit[idx]==isState:
        continue
    else:
        answer.append(isDigit[mid_idx:idx])
        mid_idx+=(idx-mid_idx)
        isState=isDigit[idx]

print(answer) # 숫자는 True, 문자는 False로 나타낸다.

answer_len=[len(i) for i in answer]
print(answer_len) # True, False로 묶인 것의 각각의 것이다.
