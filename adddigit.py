N=int(input("Enter a number:"))
t=0
while(N>0):
    dig=N%10
    t=t+dig
    N=N//10
print("The total sum of digits is:",t)
