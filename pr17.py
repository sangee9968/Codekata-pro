#input
n,k=map(int,input().split())
l=list(map(int,input().split()))
a=1
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		m=l[i]+l[j]
		if m==k:
			a=0
if a==0:
	print("yes")
else:
	print("no")
	
