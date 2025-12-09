#1)Employee salary slip 

def ems():
    name = input("Enter the name of employee: ")
    basic_sal = float(input("Enter salary of the employee: "))
    dep = input("Enter the deperment of the employee: ")

    hra = basic_sal * 0.2
    da = basic_sal * 0.1
    pf = basic_sal * 0.12

    gross = basic_sal + hra + da - pf

    print(f"HRA of the salary: {hra}\nDA of the salary: {da}\nPF of the salary: {pf}")
    print(f"Deperment: {dep}")
    print(f"Gross salary is: {gross}")

#2)Bill calculator for grocery store

def bill():
    name = input("Enter the name of product: ")
    price = int(input("Enter the price of it: "))
    quantity = int(input(f"Enter the quantity of {name}: "))

    total = price * quantity
    f_bill = total + total*0.05

    print(f"Product: {name}\nPrice: {price}\nQuantity: {quantity}")
    print(f"Total = {f_bill}")

#3)Attendence tracker for students

def att():
    st = input("Enter name of the student: ")
    sh_present = int(input("Enter the no working days: "))
    present = int(input(f"Enter no of days present for {sh_present} days: "))

    persentage = (present/sh_present)*100

    print(f"Pesentage = {persentage}%")

    if(persentage >= 75):
        print("Eligible for exams.")
    else:
        print("Not Eligible for exams.")

#4)Shopping list manager

def shop():
    li = []
    while (True):
        print("-------------------------------------------------------")
        user_input = int(input("Enter your choice\n1.Add item\n2.Remove item\n3.View item\n4.Edit\n5.Exit\n"))
        if(user_input == 5):
            break
        elif(user_input == 1):
            item = input("Enter the item name: ")
            li.append(item)
        elif(user_input == 2):
            item = input("Enter the item name to be deleted: ")
            try:
                li.remove(item)
                print(f"'{item}' deleted successfully.")
            except ValueError:
                # This code runs only if li.remove(item) fails
                print(f"Error: '{item}' not found in the list.")
        elif(user_input == 3):
            for i in li:
                print(f">>>{i}")
        elif (user_input == 4):
            testToReplace = input("Enter the old text: ")
            newChange = input("Enter the item name to be replaced: ")
            idx = li.index(testToReplace)
            li[idx] = newChange

#5)Largest and smalest number

def ls():
    def maximum(nums):
        nums.sort()
        return nums[-1]
    def minimum(nums):
        nums.sort()
        return nums[0]
    li = []

    n = int(input("Enter the range of the list: "))
    for i in range(0,n):
        item = input(f"Enter the number '{i+1}': ")
        li.append(item)
    print("Largest = ",maximum(li))
    print("Smallest = ",minimum(li))

#6)Remove duplicates

def rm():
    li = []
    new_li = []
    n = int(input("Enter the range of the list: "))
    for i in range(0,n):
        item = input(f"Enter the number '{i+1}': ")
        li.append(item)
    
    for i in li:
        if i not in new_li:
            new_li.append(i)

    for i in new_li:
        print(i)

#7)Reverse a list

def rev():
   li = []
   temp = 0
   n = int(input("Enter the range of the list: "))
   for i in range(0,n):
        item = input(f"Enter the number '{i}': ")
        li.append(item)
    
    
   for i in range(0,n//2):
       li[i] , li [n-1-i] = li[n-1-i] , li[i]
       
   for i in li:
       print(i)

#8)Find index and count

def tu():
    tup = (10,20,30,20,10,40)
    n = len(tup)
    flag1 = 20
    flag2 = 10
    count = 0

    for i in range(0,n):
        if(flag1 == tup[i]):
            idx = i
            break
    for i in range(0,n):
        if(flag2 == tup[i]):
            count = count + 1


    print(idx)
    print(count)

#9)Student record

def stu():
    students = []
    name = []
    age = []
    marks = []
    max_marks = 0
    n = 3

    for i in range(0,n):
        nam = input(f"Enter the name of student {i+1}: ")
        name.append(nam)
        ag = int(input(f"Enter the age of the student {i+1}: "))
        age.append(ag)
        mark = int(input(f"Enter the marks of the student {i+1}: "))
        marks.append(mark)
        max_marks = max(max_marks,mark)

    students = [
        (nam,ag,mark)
        for nam,ag,mark in zip(name,age,marks)
    ]

    for m in range(0,len(students)):
        if(marks[m] == max_marks):
            idx = m
    
    print("TOPPER")
    print(students[idx])

#10)Unique words

def unique():
    st = input("Enter the sentence: ").split()
    print(set(st))

#11)Common students

def com():
    A = {"Ravi", "Anu", "John"}
    B = {"John", "Meera", "Ravi"}

    print(A.intersection(B))
    print(A.difference(B))

#12)Duplicate finder

def dup():
    li = [1,2,3,2,4,3,5]
    seen = set()
    duplicates = []

    for i in li:
        if i in seen:
            duplicates.append(i)
        else:
            seen.add(i)

    print(duplicates)

#13)Attendance tracker

def track():
    s = set()
    print("Enter the students name (or 'end'to stop)")

    while(True):
       text = input(">")
       if(text == "end"):
           break
       else:
           s.add(text)
    
    print("Unique students: ",len(s))
    print("Present: ",s)

shop()