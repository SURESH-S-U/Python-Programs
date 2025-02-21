def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_rotations(n):
    s = str(n)
    return list(int(s[i:] + s[:i]) for i in range(len(s)))

def is_circular_prime(n):
    g1 = get_rotations(n)
    return all(is_prime(rot) for rot in g1)

# Example
num = int(input("Enter a number: "))
if is_circular_prime(num):
    print(f"{num} is a Circular Prime!")
else:
    print(f"{num} is NOT a Circular Prime.")
