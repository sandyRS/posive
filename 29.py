tmin = int(input("Enter time in minutes"))
m = tmin  % 60
hrs = (tmin - m) // 60
print (hrs,m)
