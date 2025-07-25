#String Method 
#string are immutable

#1.uppe() and lower() method are used to convert string in upper case and lower case respectively.
'''a= "Dhruv"
print(a.upper())  #convert string to uppercase
print(a.lower())'''  #convert string to lowercase

#using user input
'''b = input("Enter name:>")
print("This is Uppercase :>",b.upper())
print("This is Lowercase :> ", b.lower()) '''

#2. strip()
'''str = " Silver Spoon "
print(str.strip())'''

#3. rstrip()
'''print("Enter string with (!,@,$,#,%,^,&,*) ")
a = input("Enter some String with rstrip:>")
print(a.rstrip("$,#,!,@,%,^,&,*"))'''

#4. replace()
'''str = "Silver Spoon"
print(str.replace("Sp","M"))'''
 

#5 split()
'''print("Enter any string but with space..")
a = input("Enter any string:>")
print(a.split(" "))'''

#6. capitalize()
'''str = "hello"
print(str.capitalize())
str1 = "sl asokns asln"
print(str1.capitalize())'''

#7. center()
str = "Welcome to the console"
print(str.center(50))
str = "Welcome to theds console"
print(str.center(70,"."))

#8. count()
'''str = "Absaajaldjwa"
print(str.count("a"))'''

#9. endwith()
'''str = "welcome to the console"
print(str.endswith("console"))
print(str.endswith("the"))'''

#10. find()
'''str = "he's name is dhruv and he is honest man"
print(str.find("dhruv"))
str1 = "he's name is dhruv and he is HONEST MAN"
print(str.find("krishna"))'''

#11. index()
'''str =  "He's name is Dan. Dan is an honest man"
print(str.index("is"))'''

#12. isalnum()
'''str= "WelcomeToTheC90onsole"
print(str.isalnum())'''

#13. isalpha()
'''str = "Welcome"
print(str.isalpha())'''

#14. islower()
'''str = "hello word"
print(str.islower())
str1 = "Hello Word hi"
print(str1.islower())'''

#15. isprintable()
'''str = "we wish you happy diwali"
print(str.isprintable())'''

#16. isspace()
'''str= "          "
print(str.isspace())
str1 = ""
print(str1.isspace())'''

#17. istitle()
'''str = "World Health Organization"
print(str.istitle())
str1 = "world Health Organization"
print(str1.istitle())'''

#18. isupper()
'''str = "we WISH YOU HAPPY HOLLY.."
print(str.isupper())
str1 = "WE WISH YOU HAPPY HOLLY.."
print(str1.isupper())'''

#19. startwith()
'''str = "python are interesting language"
print(str.startswith("python"))
str1 = "python are interesting language"
print(str1.startswith("language"))'''

#20. swapcase()

'''str = "pytHon Are Interesting Language"
print(str.swapcase())'''

#21. title()
'''str = "he's name is dhruv. dan is honest man"
print(str.title())'''