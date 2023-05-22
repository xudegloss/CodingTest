a=[1,2,3,4,5,6,7,8,9]
size=len(a)

# 구조 분해 할당 이용하기.

for idx in range(0, (size//2)+1):
    a[idx], a[-1-idx] = a[-1-idx], a[idx]

print(a)
 
a=[1,2,3,4,5,6,7,8,9]
s, e=2, 7

# 어떤 특정 인덱스에서만 뒤집기 이용하기.

for _ in range(0, (e-s+1)//2):
    a[s-1], a[e-1] = a[e-1], a[s-1]
    s+=1
    e-=1
    
print(a)