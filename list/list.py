# Example 1
'''list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ["Red","Green","Blue","Yellow"]
print(list1)
print(list2)

print(type(list1)) '''

# Example 2
'''details = ["Dhruv",19,"BCA",7.2]
print(details) '''


# list index (positive indexing)
'''colors = ["Red", "Green", "Blue", "Yellow","Orange"]
#         0         1        2        3       4 

print(colors[0])  # prints Red
print(colors[1])  # prints Green
print(colors[2])  # prints Blue
print(colors[3])  # prints Yellow
print(colors[4])  # prints Orange '''

# list index (negative indexing)
'''colors = ["Red", "Green", "Blue", "Yellow", "Orange"]
#          -5     -4       -3          -2         -1 

print(colors[-1]) # prints Orange
print(colors[-3]) # prints Blue
print(colors[-5])  # prints Red  '''

# Check whether an item in present in the list?
'''colors = ["Red", "Green", "Blue", "Yellow", "Orange"]
if "Blue" in colors:
    print("Blue is present in the list")
else:
    print("Blue is not present in the list") '''
    
# Range of index
# Syntax:  listName[start : end : jumpIndex]
# Example: printing elements within a particular range:
'''animals = ["Dog", "Cat", "Elephant", "Lion", "Tiger", "Bear"]
print(animals[1:4])  # prints elements from index 1 to 3 (Cat, Elephant, Lion) positive indexing
print(animals[-5:-2])'''  # prints elements from index -5 to -3 (Cat, Elephant, Lion) negative indexing

# Example: printing all element from a given index till the end
'''animals = ["Dog", "Cat", "Elephant", "Lion", "Tiger", "Bear"]
print(animals[2:])  # prints elements from index 2 to the end (Elephant, Lion, Tiger, Bear)
print(animals[-4:])'''  # prints elements from index -4 to the end (Cat, Elephant, Lion, Tiger, Bear)

# List Comprehension
# Example 1: Accepts items with the small letter “o” in the new list
'''name= ["Dhruv", "Rohan", "Mohit", "Sahil", "Amit"]
name_o = [item for item in name if "o" in item]
print(name_o) '''  # prints ['Rohan', 'Mohit']

# Example 2: Accepts items which have more than 4 letters
name = ["Dhruv", "Rohan", "Mohit", "Sahil", "Amit","ram","abs"]
nameWi = [item for item in name if(len(item)<4)]
nameW = [item for item in name if(len(item)>4)]
print(nameWi)
print(nameW)