import math


print(dir(math))   # We can also use dir for the import methods



num1 = int(input())
num2 = int(input())


print(math.gcd(num1,num2))

print(math.lcm(num1,num2))


print(math.sqrt(16))  # Output: 4.0
print(math.sqrt(25))  # Output: 5.0


print(math.pow(2, 3))  # Output: 8.0
print(math.pow(5, 2))  # Output: 25.0


# math in list

import math

numbers = [2, 3.5, 4, 1.5]  # Example list
result = math.prod(numbers)
print(result)  # Output: 42.0


# or

numbers = [2, 3.5, 4, 1.5]
result = 1

for num in numbers:
    result *= num

print(result)  # Output: 42.0



