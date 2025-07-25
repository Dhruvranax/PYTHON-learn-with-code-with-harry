# 1. sort()
'''number  = [1,3,2 ,4 ,4 ,21 , 5, 6, 7, 8, 9, 10]
number.sort()
print(number)''' # prints [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]

# 2. reverse in assending order
'''number = [1,3,2 ,4 ,4 ,21 , 5, 6, 7, 8, 9, 10]
number.sort(reverse=True)
print(number)'''  # prints [21, 10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1]

# 3. reverse()
'''number = [1,3,2 ,4 ,4 ,21 , 5, 6, 7, 8, 9, 10]
number.reverse()
print(number)''' # prints [10, 9, 8, 7, 6, 5, 21, 4, 4, 2, 3, 1]

# 4. index()
'''number = [1,3,2 ,4 ,4 ,21 , 5, 6, 7, 8, 9, 10]
print(number.index(3)) '''

# 5. count()
'''colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Red"]
print(colors.count("Red"))  # prints 2
num = [1, 2, 3, 4, 5, 6,6,5, 4, 3, 2, 1]
print(num.count(2))'''  # prints 2

#6. copy()
'''num = [1, 2, 3, 4, 5, 6]
num_copy = num.copy()
print(num_copy)'''  # prints [1, 2, 3, 4, 5, 6]

# 7. append()
'''color = ["Red", "Green", "Blue", "Yellow", "Orange"]
color.append("Black")
print(color)'''  # prints ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Black']

# 8. insert()
'''color = ["Red", "Green", "Blue", "Yellow", "Orange"]
color.insert(2, "Purple")  # inserts "Purple" at index 2
print(color)'''  # prints ['Red', 'Green', 'Purple', 'Blue', 'Yellow', 'Orange']

#9. extend()
'''color =  ["Red", "Green", "Blue", "Yellow", "Orange"]
color2 = ["Black", "White"]
color.extend(color2)  # extends color list with color2
print(color)'''  # prints ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Black', 'White']

# 10. Concatenating two lists:
colors = ["Red", "Green", "Blue"]
color2 = ["Yellow", "Orange"]
print(colors + color2)  # prints ['Red', 'Green', 'Blue', 'Yellow', 'Orange']