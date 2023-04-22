N=int(input())
arr=input().split()

moves={
    "R": [0, 1],
    "L": [0, -1],
    "D": [1, 0],
    "U": [-1, 0]
}

x, y = [1, 1]
for idx in range(0, len(arr)):
    if arr[idx] in moves:
        nx = x + moves[arr[idx]][0]
        ny = y + moves[arr[idx]][1]
        if nx<1 or nx>N or ny<1 or ny>N:
            continue
        else:
            x, y = nx, ny
    print(x, y)