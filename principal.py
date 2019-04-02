from students import Students
from managing_files import Files

OPERATION = ["1: Update student's data",
            "2: Organize students files",
            "3: End program"]
print(OPERATION)
choice = input("Type operation: \n")

if (choice == "1"):

    first_name = input("Student's first name: \n")
    last_name = input("Student's last name: \n")
    student_class = input("""Type:\n2 or 3 to second and third years\n4 or 5 to forth and fifth years\n6 to sixth year.\n""")
    student_shift = input("Morning or Afternoon\n")
    presence = input("0 to not present, 1 to present:\n")
    student = Students(first_name, last_name, student_class, student_shift)
    name = student.full_name()
    format_presence = student.student_presence(presence)
    file = student.student_right_file()
    b = Files(file)
    b.append_in_file([name, format_presence])

elif (choice == "2"):
    file1 = Files("Students_presence_2_3.csv")
    file2 = Files("Students_presence_4_5.csv")
    file3 = Files("Students_presence_4_5_6.csv")
    file1.organizing_students_files()
    file2.organizing_students_files()
    file3.organizing_students_files()

elif (choice == "3"):
    print("Bye.")

else:
    raise Exception("Operation not valid.")
