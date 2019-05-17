n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,len(l)):
	for j in range(2,len(l)+1):
		s.append(sum(l[i:j:2]))
#result    
print(max(s))
		
	
