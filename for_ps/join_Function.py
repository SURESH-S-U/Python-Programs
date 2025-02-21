words = ["hello", "world"]
print(" ".join(words))


numbers = [1, 2, 3, 4]
result = ", ".join(map(str, numbers))
print(result)  # Output: "1, 2, 3, 4"


words = ['P', 'y', 't', 'h', 'o', 'n']
result = "".join(words)
print(result)  # Output: "Python"


lines = ['First line', 'Second line', 'Third line']
result = "\n".join(lines)
print(result)



words = ['This', 'is', 'a', 'test']
result = " ".join(words) + "."  # Adding a period at the end
print(result)  # Output: "This is a test."



mixed_list = ['Item', 5, 'is', 3, 'dollars']
result = " ".join(map(str, mixed_list))
print(result)  # Output: "Item 5 is 3 dollars"