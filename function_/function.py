# function in python
# geometric mean (a * b) / (a + b)
'''def calculatemean(a,b):
    mean = (a * b) / (a + b)
    print(mean)

def isgreater(a,b):
    if (a>b):
        print("first number is greater")
    else:
        print("second number is greater")

a =9
b = 4
calculatemean(a,b)
isgreater(a,b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)

c= 8
d=75
calculatemean(c,d)
isgreater(c,d)'''
# gmean2 = (c*d)/(c+d)
# print(gmean2)

# swap number
def swap(a,b):
    a,b # type: ignore
    b,a # type: ignore
    print("value of a is",a)
    print("value of b is",b)

print("number before swap")
a=5
print("value of a is",a)
b=10
print("value of b is",b)
print("\nnumber after swap")
swap(b,a)


