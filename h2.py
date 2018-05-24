l=[]
a=int(input())
for i in range(0,a):
  n=input()
  l.append(n)
  l.sort()
print("".join(l[::-1]))
