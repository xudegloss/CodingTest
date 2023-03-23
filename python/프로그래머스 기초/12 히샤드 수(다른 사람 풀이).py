# sum + list comprehension 이용하여 풀이하기
def Harshad(n):
    return n%sum(int(x) for x in str(n))==0

print(Harshad(12))