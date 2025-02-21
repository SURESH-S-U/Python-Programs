

def split_and_join(line):
    relist = []
    for char in line:
        if char == ' ':
            relist.append('-')
        else:
            relist.append(char)
    return ''.join(relist)             # Used to convert into string 

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)