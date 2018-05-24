l=[]
a=int(input())
for i in range(0,a):
  n=int(input())
  l.append(n)
for x in l:  
  if(l.count(x)==1):
    print(x) 
