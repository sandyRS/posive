symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
def check(name):
    a=0
    for i in name:
        if i in symbol:
           a=a+1
    return a           
print(check(input("Enter the String:")))
