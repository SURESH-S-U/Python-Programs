

# code 1

string = "Hello World"
substring = "World"

if substring in string:
    print("Substring is present.")
else:
    print("Substring is not present.")


# code 2

string = "Hello World"
substring = "World"

if string.find(substring) != -1:
    print("Substring is present.")
else:
    print("Substring is not present.")



# code 3

# for more than one sub  3

string = "ABCDCDC"
substring = "CDC"

count = 0
string_length = len(string)
substring_length = len(substring)

# Loop through the string
for i in range(string_length - substring_length + 1):
    # Check if the substring matches
    if string[i:i + substring_length] == substring:
        count += 1

print(f"The substring '{substring}' appears {count} times.")

