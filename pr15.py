n=int(input())
l=list(map(int,input().split()))
l1=[]
d={}
l2=[]
for i in l:
  l1.append(bin(i))
for i in l1:
  l2.append(i.count("1"))
print(l2)  
d={i:j for i in l for j in l2}
print(d)
