n=int(input())
l=[]
m=int(input())
k=[]
for i in range (0,n):
  a=int(input())
  l.append(a)
for i in range(0,m) :
  b=int(input())
  k.append(b) 
z=l+k
z.sort()
print(z)
  
