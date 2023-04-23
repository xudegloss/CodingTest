N=int(input())
plans=list(map(str, input().split()))
moves={
    "R": [0, 1],
    "L": [0, -1],
    "U": [-1, 0],
    "D": [1, 0]
}
x, y = (1, 1)

for plan in plans:
    if plan in moves:
        nx, ny = x + moves[plan][0], y + moves[plan][1]
        if nx>5 or nx<1 or ny>5 or ny<1:
            continue
        else:
            x, y = nx, ny

print(x, y)