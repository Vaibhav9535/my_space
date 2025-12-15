# 1) Student problem
class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name = ", self.name)
        print("Roll = ", self.roll)

# s1 = Student("Vaibhav","25UG00687")
# s2 = Student("Suman","25UG00576")
# s1.display()
# s2.display()

# 2) Rectangle Area problem
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2*(self.length + self.breadth)
    
# r = Rectangle(3,4)
# print(r.area())
# print(r.perimeter())

# 3) Bank Balance problem
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdrawl(self,amount):
        if amount > self.balance:
            print("No Balance")
        else:
            self.balance -= amount

    def showBalance(self):
        print(self.balance)

# b = BankAccount("Vaibhav", 2000)

# b.deposit(1000)
# b.withdrawl(4000)
# b.showBalance()

# 4) Car Milage problem
class Car:
    def __init__(self,brand,kms_run,fuel_used):
        self.brand = brand
        self.kms_run = kms_run
        self.fuel_used = fuel_used
    
    def mileage(self):
        mileage = self.kms_run / self.fuel_used
        return mileage

# c = Car("X",1000,8)
# print(c.mileage())

#5)Book Price Comparision problem
class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price
    
    def is_expensive_then(self,book2):
        if self.price > book2.price:
            return True
        return False
    
# book1 = Book("aaa",500)
# book2 = Book("bbb",400)

# print(book1.is_expensive_then(book2))