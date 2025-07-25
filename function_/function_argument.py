#1. Default argouments in functions
'''def name( fname,mname = "R",lname="Rana"):
  print("hello,",fname,mname,lname)
name("Dhruv") '''


#2. Keyword arguments in functions
'''def name(fname,mname,lname):
    print("Hello,",fname,mname,lname)
name(mname="R",lname="Rana",fname="Dhruv")'''

# 3. Required arguments in functions

# Example 1
'''def name(fname,mname,lname):
    print("Hello,",fname,mname,lname)
name("Dhruv","R")''' #TypeError: name() missing 1 required positional argument: 'lname'

# Example 2
'''def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Dhruv", "R", "Rana")'''


# 4. Variable-length arguments:
# in this 2types of variable-length arguments are used:
    #i. Arbitrary Arguments:
    #ii. Keyword Arbitrary Arguments: 


# i. Arbitrary Arguments:
'''def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")'''

# ii. Keyword Arbitrary Arguments:
'''def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")'''

# 5. Return statement in functions
def name(fname,mname,lname):
    return "Hello,"+fname+" "+mname+" "+lname
print(name("Dhruv","R","Rana"))

# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


'''def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)'''


# average(4, 6)
# average(b=9)

'''c = average(5, 6, 7, 1)
print(c)'''


# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")
