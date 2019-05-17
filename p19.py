#input
k=int(input())
l1=[]
for i in range(k):
	l=list(map(int,input().split()))
	for i in l:
		l1.append(i)
l1.sort()
print(*l1)
	
