def power(n):
    n = n/k
    if n == k:
        print("yes")
    elif n > k:
        return power(n)
    else:
        print("no") 
n=int(input())
k=int(input())
power(n)
