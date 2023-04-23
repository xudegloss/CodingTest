def findContentChildren(g, s):
    cnt=0
    g.sort()
    s.sort()
    i=0 # 아이 번호
    j=0 # 쿠키 번호

    while i<len(g) and j<len(s):
        if g[i]>s[j]:
            j+=1
        else:
            i+=1
            j+=1
            cnt+=1
    return cnt
    pass


# 아래는 수정하지 마시오.
print(findContentChildren([1,2,3], [1,1]))
print(findContentChildren([1,2], [1,2,3]))
print(findContentChildren([2,3,4], [1,5,3,1]))