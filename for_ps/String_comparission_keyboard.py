def check_same_line(s):
    top_row = set("qwertyuiop")
    home_row = set('asdfghjkl')
    bottom_row = set('zxcvbnm')
    
    # Convert string to lowercase for case-insensitive comparison
    s = s.lower()

    # Check if all characters belong to the same row
    
    if all(char in top_row for char in s):
        return "All letters are in the top row."
    elif all(char in home_row for char in s):
        return "All letters are in the home row."
    elif all(char in bottom_row for char in s):
        return "All letters are in the bottom row."
    else:
        return "Letters are from different rows."

# Example usage
input_string = "qwerty"
print(check_same_line(input_string))  # Output: All letters are in the top row.
