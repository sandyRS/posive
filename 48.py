n=int(input())
l=[]
for i in range(2, n):
    if n % i == 0 and i%2!=0:
        l.append(i)
print(*l)
