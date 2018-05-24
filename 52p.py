l=[]
a=int(input())
for i in range(0,a):
  n=int(input())
  l.append(n)
  l.sort()
k=int(input())
print(l[k-1])
