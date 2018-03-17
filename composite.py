a=int(input("Enter number: "))
if(a>1):
  for i in range(2,a):
    if(a%i==0):
      print("yes")
      break
    else:
      print("no")
      break
else:
  print("1 is neither a composite number nor prime number")
