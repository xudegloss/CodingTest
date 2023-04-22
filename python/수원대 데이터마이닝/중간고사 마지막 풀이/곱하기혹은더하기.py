# 앞이 0이거나 다음 숫자가 0 또는 1인 경우 더하기.
# 그렇지 않는 경우는 모두 곱하기.

string=input()
result=0

for idx in range(0, len(string)):
    if result==0 or int(string[idx])==0 or int(string[idx])==1:
        result+=int(string[idx])
    else:
        result*=int(string[idx])

print(result)