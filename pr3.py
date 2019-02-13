s1,s2=map(str,input().split())
l1=list(s1)
l2=list(s2)
l3=[]
for x, y in zip(s1,s2):
   if x==y:
     l2.remove(y)  
#result     
print(len(l2))
