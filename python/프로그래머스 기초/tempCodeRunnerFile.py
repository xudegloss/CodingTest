n=20
a=3
b=1
answer=0
vacant_bottle=n

while True:
    answer+=(n//a)*b
    vacant_bottle-=(n//a)*b
    n-=(n//a)*b
    if vacant_bottle==1:
        break

print(answer)