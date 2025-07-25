# print table of 10 using loop
'''for i in range(11): 
 print(i,"x",10,"=",i*10)'''

# print table of 5 using using loop
'''for i in range(1,11):
  print(5,"x",i,"=",i*5) '''

# print table of 111 using loop
'''for i in range(1,11):
    print(111,"x",i,"=",i*111)'''

# user input table of number
table = int(input("Enter the number for table:>"))
for i in range(1,11):
    print(table,"x",i,"=",i*table)