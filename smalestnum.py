n,k=list(map(int,input("enter n&k").split(' ')))
l=[]
for i in range(1,n+1):
  a=int(input("enter"))
  l.append(a)
m=sorted(l)
print(m[k-1])
