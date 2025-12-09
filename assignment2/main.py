#1)Salary increment calculator

def sal():
    salary = 50000
    for i in range(1,6):
        salary = salary + 0.1*salary
        print(salary)

#2)Shopping bill with Discount

def disc():
    n = int(input("Enter the amount of items: "))
    amt = 0
    price = 0
    discount = 0
    for i in range(0,n):
        price = float(input("Enter the price: "))
        amt = amt + price

    if(amt>=5000):
        discount = 0.2*amt
    elif(amt>=2000):
        discount = 0.1*amt
    else:
        discount = 0

    f_amt = 0
    f_amt = amt - discount
    print("The final amount = ",f_amt)

#3)Electricity bill calculator 

def e_bill():
    units = int(input("Enter your units: "))
    amt = 0
    
    if(units <= 100):
        amt = units*5
    elif(units > 100 and units <= 200):
        amt = (units-100)*7 + 100*5
    elif(units > 200):
        amt = 100*5 + 100*7 + (units-200)*10

    print(amt)

#4)Student Grade Analyser

def grade():
    n = int(input("Enter the number of subjects: "))
    t_marks = 0

    for i in range(0,n):
        marks = int(input("Enter your marks: "))
        t_marks = t_marks + marks
    
    avg = int(t_marks/n)
    print("average is: ",avg)

    if(avg >= 90):
        print("Grade is A")
    elif(avg >= 75 and avg < 90):
        print("Grade is B")
    elif(avg >= 60 and avg < 75):
        print("Grade is C")
    else:
        print("Fail")

#5)ATM withdrawal simulation

def atm():
    balance = 10000
    t_balance = balance
    r_amt = 0
    while(t_balance != 0 and t_balance > 0):
        r_amt = int(input("Enter the amount required: "))
        if(t_balance < 1000):
            print("low balance")
        t_balance -= r_amt
    if(r_amt > t_balance):
        print("Insufficient Balance")

#6)Pyramid

def pattern():
    n = int(input("Enter n value"))
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("")
