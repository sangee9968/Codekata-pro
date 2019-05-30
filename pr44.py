#input
n,p,q,r=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
	for j in range(i,n):
		for k in range(j,n):
			a=(p*l[i])+(q*l[j])+(r*l[k])
			l1.append(a)
print(max(l1))
