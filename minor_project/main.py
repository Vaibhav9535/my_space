#COLLEGE COURSE REGISTRATION AND ATTENDENCE TRACKING SYSTEM

#permanent data 
courses = ["Python", "Java", "DBMS", "Maths", "Physics"]
course_codes = {"PY101", "JV102", "DB103", "MA104", "PH105"}

#inital students
students = { 
    101: {
        "name": "Kiran", 
        "courses": ["Python", "DBMS"],
        "attendence":("2025-02-10", "Present")
        }, 
    102: {
        "name": "Meera", 
        "courses": ["Java", "Maths"],
        "attendence":("2025-02-10", "Present")
        }
}

#functions section
def display():
    for i,j in zip(sorted(courses),sorted(list(course_codes))):
        print(f"{i}-->>{j}")

def new_student():
    roll_no_start = list(students.keys()).pop() + 1
    print("Enter the name of the new student")
    while True:
        new_student_name = input()
        if any(ch.isdigit() for ch in new_student_name):
            print("Try again!!!!")
        else:
            break    
    new_student_courses = list()
    display()
    num_of_courses = 0

    while num_of_courses != 2:
        txt = input("Enter the course name: ")
        if txt in courses:
            new_student_courses.append(txt)
            num_of_courses += 1
        else:
            print("Invalid course try again!!!")

    students[roll_no_start] = {"name":new_student_name,"courses":new_student_courses,"attendence":"NONE"}

def mark_attendance():
    name_toAttend = input("Enter the name of the student: ")
    for key1,value1 in students.items():
        for kye2,value2 in value1.items():
            if name_toAttend == value1["name"]:
                rollNo_toAttend = key1
                break
    date = input("Enter the date: ")
    val = int(input("present(1)/absent(0)"))
    if val==1:
        students[rollNo_toAttend]["attendence"] = (date,"Present")
    else:
        students[rollNo_toAttend]["attendence"] = (date,"Absent")

def student_summary():
    print("STUDENT RECORD")
    for stu_id,details in students.items():
        print(f"--- Student ID:{stu_id} ---")
        print(f"Name: {details["name"]}")
        print(f"Courses: {', '.join(details["courses"])}")
        print(f"Attendence: {details["attendence"]}")

def edit():
    ID = int(input("Enter the ID of the student: "))
    print("name :- ",students[ID]["name"])
    print("Current courses :-",students[ID]["courses"])
    oldCourse = input("Enter the old course to be changed: ")
    newCourse = input("Enter the new course: ")

    idx = students[ID]["courses"].index(oldCourse)

    students[ID]["courses"][idx] = newCourse


def menu():
    print(".............MENU.............")
    print("1) Display courses and their codes")
    print("2) Register a new student")
    print("3) Mark attendence")
    print("4) Students summary")
    print("5) Edit course")
    print("6) Exit")

menu()

while(True):
    print("ENTER>>>",end="")

    n = int(input())

    if n == 1:
        display()
        print()
    elif n == 2:
        new_student()
        print()
    elif n == 3:
        mark_attendance()
        print()
    elif n == 4:
        student_summary()
        print()
    elif n == 5:
        edit()
        print()
    elif n == 6:
        break