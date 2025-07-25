# tuples are imuatable 
'''color = ("red","green","blue")
print(type(color))
print(color) '''

# Accessing tuple items:
# 1. Positive Index
'''country= ("india","russia","srilanka")
print(country[0]) # prints "india"
print(country[1]) # prints "russia"
print(country[2]) # prints "srilanka" '''

# 2. Negative Index
'''country= ("india","russia","srilanka")
print(country[-1]) # prints "srilanka"
print(country[-2]) # prints "russia"
print(country[-3]) # prints "india" '''

# 3. check for item:
'''country=("india","spain","russia","italy")
if "spain" in country:
    print("spain in this country")
else:
    print("spain is not in the country") '''
    
# 4. Range of Index
# Example: Printing elements within a particular range:
'''animals =("cat","dog","mouse","rat","hourse","tiger","lion","pig","cow","goat")
print(animals[3:7]) # prints ('rat', 'hourse', 'tiger', 'lion')
print(animals[-7:-2]) # prints ('rat', 'hourse', 'tiger', 'lion', 'pig')'''

# Example: Printing all element from a given index till the end
'''animals =("cat","dog","mouse","rat","hourse","tiger","lion","pig","cow","goat")
print(animals[4:])  #('hourse', 'tiger', 'lion', 'pig', 'cow', 'goat')
print(animals[-4:]) #('lion', 'pig', 'cow', 'goat') '''

'''countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)'''

# Tuple method 
# 1. count() method
'''d = (0,1,2,4,5,3,5,7,8,9,10,12)
res= d.count(5)
print('count of 5 is ',res)'''


# 2. index() method
tuple=(0, 1, 2, 3, 2, 3, 1, 3, 2)    
res = tuple.index(3)
print('first occurrence of 3 is ', res)

 