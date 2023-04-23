s=input()
result=0

for idx in range(0, len((s))):
    if result==0 or int(s[idx])==0 or int(s[idx])==1:
        result+=int(s[idx])
    else:
        result*=int(s[idx])

print(result)