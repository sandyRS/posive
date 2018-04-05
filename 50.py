a= int(input("enter"))
if a>1:
   for i in range(2,a):
       if (a % i) == 0:
           print("Yes")
           break
       else:print("no")
else:print("enter greater than one")
