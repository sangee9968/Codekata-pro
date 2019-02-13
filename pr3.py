s1,s2=map(str,input().split())
l1=list(s1)
l2=list(s2)
for x, y in zip(s1,s2):
  if len(s1)>len(s2) and x==y:
    l1.remove(y)
    print(len(l1))
  else:
    break
for x, y in zip(s1,s2):  
  if len(s1)<=len(s2) and x==y:
    l2.remove(y)
#result      
print(len(l2))
  
