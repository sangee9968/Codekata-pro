n=int(input())
l=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096]
if n&(n-1)==0:
	print("0")
l1=[]
if n&(n-1)!=0 :
	for i in l:
		if n>i:
			l1.append(i)
#result			
print(n-max(l1))    

	
