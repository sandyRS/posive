l=[]
s=[]
a=int(input())
for i in range(1,a+1):
  n=int(input())
  l.append(n)
for i in l:
  a=l.index(i)  
  if(i==a):
    s.append(i)
print("".join(str(i) for i in s))
