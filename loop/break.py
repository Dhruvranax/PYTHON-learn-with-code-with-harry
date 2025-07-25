# break statement

'''for i in range(5):
    if i == 3: # condition to break the loop
        break #when condition is i==3 , loop will break and will not execute the next line
    print(i)'''

for i in range(1,101,1):
    print(i,end=" ")
    if(i==50):
        print("hi bhow bhow") # when i is 50 it will print hi bhow bhow and then continue the loop
        break
    else:
        print("no miyaw miyaw") #it will print no miyaw miyaw till 50 and then it will break the loop and print hi
print("bhoooow bhoow bhow") #this will print after the loop is broken
