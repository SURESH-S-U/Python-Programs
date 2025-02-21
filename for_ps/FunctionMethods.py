
def get_user_info():
    name = "Suresh"
    age = 21
    return name, age  # Returning multiple values as a tuple

name, age = get_user_info()
print(f"Name: {name}, Age: {age}")


#================================================================================

def add_numbers(*args):
    return sum(args)

result = add_numbers(1, 2, 3, 4)
print(f"Sum: {result}")


#===================================================================================


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Call the recursive function
result = factorial(5)
print(f"Factorial: {result}")


#===================================================================================

#Using Tuple

def process_arrays():
    array1 = [1, 2, 3, 4, 5]
    array2 = [6, 7, 8, 9, 10]
    return array1, array2  # Returning two arrays as a tuple

# Call the function and unpack the arrays
arr1, arr2 = process_arrays()
print("Array 1:", arr1)
print("Array 2:", arr2)


#====================================================================================

def process_arrays():
    array1 = [11, 12, 13, 14, 15]
    array2 = [16, 17, 18, 19, 20]
    return [array1, array2]  # Returning two arrays as a list

# Call the function and unpack the arrays
arrays = process_arrays()
print("Array 1:", arrays[0])
print("Array 2:", arrays[1])


