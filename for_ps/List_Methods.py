# Creating a list
my_list = [1, 2, 3, 4, 5]

# append: Adds an element to the end of the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# clear: Removes all elements from the list
my_list.clear()
print(my_list)  # Output: []

# copy: Returns a shallow copy of the list
my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 2, 3]

# count: Returns the number of occurrences of an element
print(my_list.count(2))  # Output: 1

# extend: Adds all elements of another iterable (like a list) to the end of the list
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

# index: Returns the index of the first occurrence of an element
print(my_list.index(3))  # Output: 2

# insert: Inserts an element at a specific index
my_list.insert(2, 'new')  # Inserts 'new' at index 2
print(my_list)  # Output: [1, 2, 'new', 3, 4, 5]

# pop: Removes and returns an element at the specified index (default is -1)
removed_element = my_list.pop()
print(removed_element)  # Output: 5
print(my_list)  # Output: [1, 2, 'new', 3, 4]

# remove: Removes the first occurrence of an element
my_list.remove('new')
print(my_list)  # Output: [1, 2, 3, 4]

# reverse: Reverses the list
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]

# sort: Sorts the list (in-place by default)
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]



# Creating a list
my_list = [1, 2, 3]

# __add__: Used for the "+" operator
new_list = my_list.__add__([4, 5])  # Equivalent to my_list + [4, 5]
print(new_list)  # Output: [1, 2, 3, 4, 5]

# __getitem__: Used for indexing
print(my_list.__getitem__(1))  # Output: 2 (second element)

# __len__: Used for len()
print(my_list.__len__())  # Output: 3

# __eq__: Used for equality comparison
print(my_list.__eq__([1, 2, 3]))  # Output: True

# __str__: Used for str() or print
print(my_list.__str__())  # Output: [1, 2, 3]



#   list minimum maximuim methods

print(max(3, 1, 4, 2))  # Output: 4
print(max([5, 2, 9, 1, 7]))  # Output: 9
print(max("hello"))


print(min(3, 1, 4, 2))  # Output: 1
print(min([5, 2, 9, 1, 7]))  # Output: 1
print(min("hello"))  # Output: 'e' (smallest character by ASCII)

