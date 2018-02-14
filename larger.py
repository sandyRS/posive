n=int(input('enter your input'))
e=int(input('enter 2-nd input'))
c=int(input('enter 3-rd input'))
if(n>e):
    if(n>c):
        print('n is larger')
    else:
        if(e>c):
            print('e is larger')
        else:
            print('c is larger')
