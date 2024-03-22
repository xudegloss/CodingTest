# 최대공약수 만들기 -> answer1
# 최소공배수 만들기 -> answer2

# 3 / 12 -> 1, 3 / 1, 2, 3, 4, 6, 12
# 최대공약수 => 약수 중에서 제일 큰 거
# 최소공배수 => 12의 배수가 3으로 나눠지는지 체크

# 2 / 5 -> 1, 2 / 1, 5
# 최대공약수 => 없는 경우 1
# 최소 공배수 => 5의 배수가 2로 나눠지는지 체크

"""
왜 틀린지 잘 모르겠음...
    
"""

def solution(n ,m):
    # 1. 최대공약수 구하기
    n_list=[] # n의 공약수 모음
    m_list=[] # m의 공약수 모음
    
    for n_num in range(1, n+1):
        if n%n_num==0:
            n_list.append(n_num)
    
    for m_num in range(1, m+1):
        if m%m_num==0:
            m_list.append(m_num)
        
    answer_max=[]    
    for i in range(len(m_list)):
        if m_list[i] in n_list:
            answer_max.append(m_list[i])
    answer1= max(answer_max)
    
    # 2. 최소공배수 구하기
    i=1
    answer2=0
    
    if m<n:
        m,n = n,m
        
    while True:
        m=m*i
        if m%n==0:
            answer2=m
            break
        i+=1
            
        
    answer=[]
    answer.append(answer1)
    answer.append(answer2)
    
    return answer