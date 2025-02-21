
# we can get 1 liters from 2 slots (hot,cold,norm) oresle we can get 1 liter from 1 slot.
# we have to find the minimum time to get all water from the slots.



def getWater(a):

    tot_time = 0
    
    if a[0] < a[1]:
        time = a[0]
        rem = a[1] - a[0]
    else:
        time = a[1]
        rem = a[0] - a[1]

    tot_time += time

    if rem < a[2]:
        time = rem
        rem2 = a[2] - rem
    else:
        time = a[2]
        rem2 = rem - a[2]

    tot_time += time + rem2

    return tot_time


print("Enter the list : ")
lst = list(map(int,input().split(",")))

print(getWater(lst))