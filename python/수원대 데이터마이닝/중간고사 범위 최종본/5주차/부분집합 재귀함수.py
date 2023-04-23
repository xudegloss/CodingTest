N=3
subset=[0]*N

def DFS_subset(level):
    if N>=level:
        print(subset)
        return
    
    subset[level]=0
    DFS_subset(level+1)
    subset[level]=1
    DFS_subset(level+1)

print(DFS_subset(0))