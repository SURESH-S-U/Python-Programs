
s = "Hello, World!"

print(s[0:5])   # Output: Hello
print(s[7:])    # Output: World!
print(s[:5])    # Output: Hello
print(s[-6:])   # Output: World!

print(s[::-1])   # for reverse the string



s = "Hello, World!"
index = s.find("World")
print(index)  # Output: 7


s = "Hello, World!"
print("World" in s)   # Output: True
print("Python" in s)  # Output: False


s = "apple,banana,grape"
parts = s.split(",")
print(parts)  # Output: ['apple', 'banana', 'grape']
print(parts[1]) 


