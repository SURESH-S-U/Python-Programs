def bubble_sort_dec(students):
    n = len(students)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if students[j][1] < students[j + 1][1]:

                students[j], students[j + 1] = students[j + 1], students[j]

def bubble_sort_ass(students):
    n = len(students)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if students[j][1] > students[j + 1][1]:

                students[j], students[j + 1] = students[j + 1], students[j]

num_students = int(input("Enter the number of students: "))
students = []

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    rank = int(input(f"Enter the rank of {name}: "))
    students.append((name, rank))

print("\nMenu:")
print("1. Sort by rank in ascending order")
print("2. Sort by rank in descending order")

choice = input("Enter your choice (1/2/3): ")
if choice == "1":
    bubble_sort_ass(students)

elif choice == "2":
    bubble_sort_dec(students)  

else:
        print("Invalid choice! Please try again.")


print("\nStudents sorted by rank in descending order:")
for student in students:
    print(f"Name: {student[0]}, Rank: {student[1]}")
