s1,s2=map(int,input("enter").split(' '))
m=0
for i in range(s1,s2+1):
  if(i%2!=0):
    m=m+i
print(m)
