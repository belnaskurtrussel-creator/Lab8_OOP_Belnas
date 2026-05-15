print ("1.)")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Car: {self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.display_info())



print ("2.)")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_info(self):
        return f"Student: {self.name}, Grade: {self.grade}"

student1 = Student("Allen", "A")
print(student1.get_info())



print ("3.)")

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.__balance += amount
        return f"New Balance: {self.__balance}"

    def get_balance(self):
        return f"Balance: {self.__balance}"

account = BankAccount("John Doe", 1000)
print(account.deposit(500))
print(account.get_balance())



print ("4.)")

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

dog = Dog()
print(dog.speak())



print ("5.)")

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def fuel_type(self):
        return "Uses gasoline"

class ElectricCar(Car):
    def fuel_type(self):
        return "Uses electricity"

tesla = ElectricCar()
print(tesla.move())
print(tesla.fuel_type())



print ("6.)")

class Device:
    def power_on(self):
        return "Device is turning on"

class Smartphone(Device):
    def power_on(self):
        return "Smartphone is booting up"

phone = Smartphone()
print(phone.power_on())



print ("7.)")

class Box:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        return Box(self.weight + other.weight)

box1 = Box(5)
box2 = Box(10)
box3 = box1 + box2
print(f"Total weight: {box3.weight} kg")



print ("8.)")

from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        return "Fan is spinning"

fan = Fan()
print(fan.turn_on())



print ("9.)")

class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def roll(self):
        return "Wheels rolling"

class Car(Engine, Wheels):
    def drive(self):
        return "Car is moving"

my_car = Car()
print(my_car.start())
print(my_car.roll())
print(my_car.drive())



print ("10.)")

class MathOperations:
    @staticmethod
    def square(num):
        return num * num

number = int(input("Enter a number: "))
print("Square:", MathOperations.square(number))



print ("11.)")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author}"

book1 = Book("1984", "George Orwell")
print(book1.get_info())



print ("12.)")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name} costs ${self.price}"

product1 = Product("Laptop", 1200)
print(product1.get_details())



print ("13.)")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

p = Person("Alice")
print(p.greet())



print ("14.)")

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawn {amount}, Remaining balance: {self.balance}"

atm = ATM(1000)
print(atm.withdraw(200))



print ("15.)")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

emp1 = Employee("Michael", 5000)
print(emp1.display())



print ("16.)")

class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def get_info(self):
        return f"Patient: {self.name}, Age: {self.age}, Disease: {self.disease}"

patient1 = Patient("John Cruz", 45, "Diabetes")
print(patient1.get_info())



print ("17.)")

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}"

teacher1 = Teacher("Mr. Smith", "Mathematics")
print(teacher1.teach())



print ("18.)")

class Flight:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination

    def book_ticket(self):
        return f"Ticket booked for flight {self.flight_number} to {self.destination}"

flight1 = Flight(101, "Tokyo")
print(flight1.book_ticket())



print ("19.)")

class SmartDevice:
    def __init__(self, device_name, status="Off"):
        self.device_name = device_name
        self.status = status

    def turn_on(self):
        self.status = "On"
        return f"{self.device_name} is now {self.status}"

light = SmartDevice("Living Room Light")
print(light.turn_on())



print ("20.)")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        return f"Book '{title}' added to the library"

    def show_books(self):
        return f"Available Books: {', '.join(self.books)}"

library = Library()
print(library.add_book("Python Programming"))
print(library.show_books())