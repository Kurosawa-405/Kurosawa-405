student_list1 = ['andrew', 'chris', 'martha', 'tristian', 'bigjoe']
student_list2 = ['madmax', 'vansh', 'tate']

def student_list(student_list1, student_list2):
    for student in student_list2:
        for i in student_list1:
            if i == 'chris':
                print(f"where is {i}")

student_list(student_list1, student_list2)