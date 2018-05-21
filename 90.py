lis=list(input())
k=[]
for x1 in lis:
    if x1.isdigit():
        k.append(x1)
print("".join(str(n) for n in k))
