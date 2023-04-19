# c2 : 6가지
# a1 : 2가지

def solution(c): # 좌표
    ## 움직일 수 있는 모든 경로 표현하기.
    dx=[2, 2, -2, -2, 1, -1, 1, -1]
    dy=[1, -1, 1, -1, 2, 2, -2, -2]

    ## 현재 위치 (row, col)
    x, y = int(c[1]), ord(c[0])-96
    
    cnt=0 # 움직일 수 있는 모든 경우
    ## 움직일 수 있는 경우를 모두 세기.
    for iter in range(0, len(dx)):
        nx=x+dx[iter]
        ny=y+dy[iter]
        if nx<1 or ny<1 or nx>8 or ny>8:
            continue
        cnt+=1
    return cnt

    
print(solution("c2")) # 6
print(solution("a1")) # 2