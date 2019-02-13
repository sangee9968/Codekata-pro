a,b=map(str,input().split())
if len(a)<len(b):
    k=len(a)
else:
    k=len(b)
c=0
for i in range(0,k):
    if a[i]!=b[i]:
        c=c+1
    else:
        c=c+0
if len(a)<len(b) or len(a)>len(b):
    k=abs(len(a)-len(b))
    c=c+k
#result    
print(c)

    
