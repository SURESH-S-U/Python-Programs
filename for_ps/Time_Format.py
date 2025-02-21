def time(lst):
    if int(lst[0]) > 12:
        if int(lst[0]) <= 21:
            lst[0] = "0" + str(int(lst[0]) - 12)
        else:
            lst[0] = str(int(lst[0]) - 12)

        lst[3] = "PM"
    
    else:
        lst[3] = "AM"

    
    return "-".join(lst)



time_str = input("Enter the  string : ")

lst = time_str.split("-")

print(dir(lst))
