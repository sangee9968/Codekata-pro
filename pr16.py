#input
n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
sum=0
for i in range(0,len(l)):
		sum=sum+k.index(l[i])+1
print(sum)	
	
	
