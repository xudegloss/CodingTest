def solution(seoul):
    for idx in range(0, len(seoul)):
        if "Kim" in seoul[idx]:
            return f"김서방은 {idx}에 있다"