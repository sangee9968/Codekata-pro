import math
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
g,h=map(int,input().split())
w=math.sqrt(abs((b-a))**2+abs((d-c))**2)
x=math.sqrt(abs((d-c))**2+abs((f-e))**2)
y=math.sqrt(abs((f-e))**2+abs((h-g))**2)
z=math.sqrt(abs((h-g))**2+abs((b-a))**2)
if w==x and y==z and x==z:
	print("yes")
else:
  #result
	print("no")
