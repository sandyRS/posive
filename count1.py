number = int(input("Please Enter any Number: "))
Count = 0
while(number > 0):
    number = number // 10
    Count = Count + 1
    print" Number of Digits in a Given Number ", Count
