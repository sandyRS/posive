n=input("Enter Alphanumeric")
a=0
b=0
for i in n:
    if(i.isdigit()):
      a=a+1
    if(i.isalpha()):
      b=b+1
      if(a>0 and b>0):
         print('yes')
         break
if(a==0 or b==0):
  print('No')
      
