a=input()
b=input()
l=[]
for i in range(0,len(a)):
  if(a[i]==b[i]):
    l.append(a[i])
  else:
    break
print("".join(str(x)) for x in l)  
