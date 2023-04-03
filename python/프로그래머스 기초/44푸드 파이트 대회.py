def solution(food):
    answer = []
    food_num=1

    for idx in food[1:]:
        i=0
        while True:
            if i==idx//2:
                break
            answer.append(food_num)
            i+=1
        food_num+=1
    answer_list=answer+[0]+answer[::-1]

    # 하나 하나 반복문 돌려서 문자열로 만들어주기
    return "".join(str(s) for s in answer_list)

print(solution([1,7,1,2]))