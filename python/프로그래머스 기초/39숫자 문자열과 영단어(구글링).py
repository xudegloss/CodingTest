def solution(s):
    dic={"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, 
         "six":6, "seven":7, "eight":8, "nine":9, "ten":10}
    answer = s
    for i in dic.items():
        answer=answer.replace(i[0], str(i[1]))
    return int(answer)
