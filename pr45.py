#input
n=input()
a=1
if n==n[::-1]:
	print("yes")
else:
	m=n.strip("0")
if m==m[::-1]:
	a=0
if a==0:
	print("yes")
else:
	print("no")
