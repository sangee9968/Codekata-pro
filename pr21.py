#input
n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
x=1
for i in range(0,len(l)-1):
	l1.append(l[0:i+1])
	l2.append(l[i+1:])
for i in l1:
	for j in l2:
		a=sum(i)/len(i)
		b=sum(j)/len(j)
		if a==b:
			x=0
if x==0:
	print("yes")
else:
	print("no")
