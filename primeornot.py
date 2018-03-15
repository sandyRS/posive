a=int(input("enter your input"))
if a>1:
  for i in range (2,a):
    if(a%i==0):
      print("not a prime number")
      break
  else:
    print("prime number")
