#1)name tag generator

def nameTag():
    name = input("Enter your name: ")
    words = name.split(' ')

    first = words[0]
    last = words[-1]

    res = first[0:3] + last[-3:]
    res = res.upper()
    print(res)


#2)mobile username creator

def nameNum():
    name = input("Enter your name")
    phno = input("Enter your ph no")

    words = name.split(' ')

    res = words[0] + '_' + phno[-4:]
    print(res)

#3)shop bill calculator

def gst():
    price = int(input("Enter the amount: "))
    quantity = int(input("Enter the quantity: "))

    total = price * quantity

    total += 0.05 * total

    print(total)

#4)student result checker

def result_checker():
    marks = int(input("Enter the marks: "))
    attendance = int(input("Enter the attendance: "))

    if(marks >= 35 and attendance >= 75):
        print("Pass")
    else:
        print("Fail") 

#5)Password verification system

def pwdVerification():
    test = True
    while(test):
        pwd1= input("Enter the passowrd it should have @ symbol and should have 8 or more characters: ")
        pwd2= input("Enter again: ")

        if(len(pwd1) >= 8 and '@' in pwd1 and pwd1 == pwd2):
            print("Password accepted")
            test = False
        else:
            print("Password invalid")

#6)Electricity bill estimator 

def eBill():
    units = int(input("Enter your units: ")) 

    if(units <= 100):
        amt = units*2
    elif(units > 100 and units <=200):
        amt = (units-100)*3 + 100*2
    elif(units > 200):
        amt = (units-200)*5 + 100*3 + 100*2
    print(amt)
