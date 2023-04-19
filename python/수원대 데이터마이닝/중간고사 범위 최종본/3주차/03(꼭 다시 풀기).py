## (row, col)
## dictionary와 replace 이용하기.

def move_plans(n, plans):
    plans=list(plans.replace(" ","")) # 계획 리스트로 변경하기.
    
    x, y = (1, 1) # 현재 위치 : 튜플로 나타내기.
    
    # 움직이는 방법
    moves={
        "U" : (-1, 0),
        "D" : (1, 0),
        "L" : (0, -1),
        "R" : (0, 1)
    }

    for plan in plans:
        # 새로운 위치의 x, y 구하기.
        if plan in moves:
            nx=x+moves[plan][0]
            ny=y+moves[plan][1]

        # 공간을 넘어가면 그냥 코드 무시하기.
        if nx<1 or ny<1 or nx>n or ny>n:
            continue 

        # 그렇지 않으면 새롭게 x, y 갱신하기.
        x, y = nx, ny 
    return x, y  
    pass

print(move_plans(5, 'D D L R U U U'))
print(move_plans(5, 'R R R U D D'))