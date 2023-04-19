def findContentChildren(g, s):
    i=0 # 아이 번호
    j=0 # 쿠키 번호
    g.sort()
    s.sort()
    result=0

    while i<len(g) and j<len(s):
        print(i, j)
        if g[i]<=s[j]: # 아이를 만족시키는 경우
            result+=1
            i+=1
            j+=1
        else: # 아이를 만족시키지 못하는 경우
            j+=1
    return result
    pass

# 아래는 수정하지 마시오.
print(findContentChildren([1,2,3], [1,1]))
print(findContentChildren([1,2], [1,2,3]))
print(findContentChildren([2,3,4], [1,5,3,1]))
