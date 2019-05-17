#input
s=input()
for i in range(0,len(s)-1):
	for j in range(i+1,len(s)+1):
		if ord(s[j])>ord(s[i]):
			print(s[j:])
