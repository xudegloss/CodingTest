# 8 X 8 좌표 평면
s=input()
row=int(s[1])
col=int(ord(s[0]))-96
moves={
    "m1": [-2, -1],
    "m2": [-2, 1],
    "m3": [-1, 2],
    "m4": [1, 2],
    "m5": [-1, -2],
    "m6": [1, -2],
    "m7": [2, 1],
    "m8": [2, -1],
}

cnt=0
for move in moves:
    nr, nc = row + moves[move][0], col + moves[move][1]
    if nr>8 or nr<1 or nc>8 or nc<1:
        continue
    else:
        cnt+=1

print(cnt)