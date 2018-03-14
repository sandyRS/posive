n = int(input("enter num of turns"))
n1 = 0
n2 = 1
count = 0
if n <= 0:
   print("Please enter a positive value")
elif n== 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence upto",n,":")
   while count < n:
       print(n1,end=' , ')
       n3 = n1 + n2
       # update values
       n1 = n2
       n2 = n3
       count= count+1
