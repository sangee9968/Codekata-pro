from itertools import combinations
n,k=map(int,input().split())
s=len(str(n))
l=list(combinations(str(n),s-k))
l=sorted(l)
#result
print("".join(l[0]))
