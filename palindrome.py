a=int(input("enter your number"))
temp=a
rev=0
while(a>0):
  dig=a%10
  rev=rev*10+dig
  a=a//10
if(temp==rev):
  print("yes,number is palindrome")
else:
  print("no,number is not palindrome")
  
