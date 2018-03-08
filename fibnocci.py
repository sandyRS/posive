N = int(input("\nPlease Enter the Range Number: "))
i = 0
F= 0
S = 1
while(i < N):
  if(i <= 1):
    Next = i
  else:
        Next = F + S
        F= S
        S = Next
  print(Next)
  i = i + 1
