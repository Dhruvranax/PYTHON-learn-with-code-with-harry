
'''x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case 3:
        print("x is three")
    case 4:
        print("case is 4")
    case _:
         print("invalid value😂")'''

# case with if condition..
import time
timestamp = time.strftime('%H:%M')
print(timestamp)
a=int(input("Enter you number:>"))
match a:
    case _ if a==0:
        print("a is zero")
    case _ if a==90:
        print("a is 90")
    case _ if a>90:
        print("a is greater than 90")
    case _ if a<90:
        print("a is less than 90")
    case _:
        print("invalid choose.")
        