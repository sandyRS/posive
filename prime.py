a=int(input("Enter number: "))
if(a>1):
  for i in range(2,a):
    if(a%i==0):
      print("given number not is prime")
      break
    else:
      print("given number  prime number")
     
     
