s="dhoni"
s1=input()
l=list(s)
l1=list(s1)
if all(i in l1 for i in l) and len(l)==len(l1):
  print("yes")
else:
  #result
  print("no")  
