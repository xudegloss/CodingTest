import sys
import os

current_path=os.getcwd()
sys.stdin=open(current_path + "//python//코딩테스트 강의 내용//01 코드 구현력//" + "input.txt")

N, M = map(int, input().split())
new_list=[]
for i in range(1, N+1):
    for j in range(1, M+1):
        new_list.append(i+j)

new_dict={}
for num in new_list:
    if num not in new_dict:
        new_dict[num]=num
        new_dict[num]=1
    else:
        new_dict[num]+=1

max_value=max(new_dict.values())

for key, value in new_dict.items():
    if value ==max_value:
        print(key, end=" ")


"""
### list로도 풀 수 있다. 굳이 dict으로만 풀 이유가 없다. ###
cnt = [0] * (N+M+3)

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j]+=1

max=-2147000000
for i in range(0, len(cnt)):
    if cnt[i] > max:
        max=cnt[i]

for i in range(0, len(cnt)):
    if cnt[i]==max:
        print(i, end=" ")
"""