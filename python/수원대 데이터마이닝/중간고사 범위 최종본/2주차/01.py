n=int(input())
coins=[500, 100, 50, 10]
cnt=0

for coin in coins:
    if n >= coin:
        cnt+=n//coin
        n-=(n//coin)*coin # n %= coin도 가능하다.
print(cnt)