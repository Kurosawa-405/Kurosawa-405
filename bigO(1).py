student_list1=['andrew','tristiam','martha','liam','bigjoe']
def student_list(student_list1):
    print(student_list1[0])
    print(student_list1[1])
student_list(student_list1)

for i in range(len(student_list1)):
    n=int(input(("Enter the number of students: ")))
    if n < 0:
        print("Please enter a valid number of students.")
    else:
        print(f"Number of students: {n}")
        break
    