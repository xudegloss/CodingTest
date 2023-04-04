# 1, 3, 5, 7, 8, 10, 12 : 31일
# 2 : 29일
# 4, 6, 9, 11 : 30일

day=["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
mon=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 5 / 24 : 화요일
# 1 / 1 : 금요일

a=5
b=24

days=(sum(mon[: a-1])+b)%7
print(day[days])

## 고려해야할 점
# 1. 한꺼번에 날짜를 구하여 7로 나눈 후에 해당 요일을 구해야 한다.
# 2. 그러기 위하여 day의 인덱스 요일을 제대로 맞춰주기 (1월 1일은 금요일 이용하기)
# 3. sum 같은 내장 함수 이용 열심히 하기. 

def solution(a, b):
    day=["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    mon=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # days=(sum(mon[:a-1]+b))%7
    days=(sum([d for d in mon[: a-1]])+b)%7
    return day[days]

print(solution(5, 24))