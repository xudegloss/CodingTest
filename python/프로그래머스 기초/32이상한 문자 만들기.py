##### 문제 잘 읽기! 인덱스 기준이 아니라, 공백 기준! #####
# def solution(s):
#     s=list(s)
#     answer = []
    
#     for idx, str in enumerate(s):
#         if idx%2==0:
#             answer.append(str.upper())
#         else:
#             answer.append(str.lower())
#     return "".join(answer)


# s=list("try hello world")
# print(s)
# vacant_list=[]

# for idx, str in enumerate(s):
#     if idx%2==0:
#         vacant_list.append(str.upper())
#     else:
#         vacant_list.append(str.lower())

# print("".join(vacant_list))

# s="try hello world".split(" ")
# vacant_list=[]

##### 공백 기준으로 풀이하기. #####
# for iter in range(len(s)):
#     for idx, str in enumerate(s[iter]):
#         print(idx, str)
#         if idx%2==0:
#             vacant_list.append(str.upper())
#         else:
#             vacant_list.append(str.lower())
#     vacant_list.append(" ")
# print("".join(vacant_list))

def solution(s):
    s=s.split(" ")
    vacant_list=[]

    for iter in range(len(s)):
        for idx, str in enumerate(s[iter]):
            if idx%2==0:
                vacant_list.append(str.upper())
            else:
                vacant_list.append(str.lower())
        if iter<len(s)-1:
            vacant_list.append(" ")
    return "".join(vacant_list)