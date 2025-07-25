num = int(input("Enter Number:>"))
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<10):
        print("Number is less than 10")
    elif(num>10 and num<=20):
        print("Number is between 10 and 20")
    else:
        print("Number is grather than 20")
else:
    print("Number is zero")
