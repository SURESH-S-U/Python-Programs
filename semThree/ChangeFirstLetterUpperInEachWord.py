import os
def solve(s):

    s = list(s)
    

    if s[0].isalpha():
        s[0] = s[0].upper()
    

    for i in range(1, len(s)):
        if s[i-1] == " " and s[i].isalpha():
            s[i] = s[i].upper()
    

    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
