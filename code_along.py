#importing!
#import module 
#import math #whole module
from math import pi, sqrt # just pi!
#import with an alias!
import datetime as dt
from module import say_hello
#pi = math.pi # whole module how to call

pie = pi #calling just the function
print(dt.datetime.now())
#create a student class!

#what do all students have? They have a name, birthday, major

#what can a student do? they can study, stop studying, celebrate their birthday

class Student():
    def __init__(self, name, birthday, major="Computer Science"):
        self.name = name
        self.birthday = birthday
        self.major = major
        self.is_studying = False # they arent studying right away
        self.university = "CSU"

    def study(self):
        self.is_studying = True
        print(f'{self.name} is studying {self.major}')

    def stop_studying(self):
        self.is_studying = False
        print(f"{self.name} is very tired and has stopped studying for now.")

    def celebrate_birthday(self):
        print(f"Happy Birthday {self.name}! you are now {self.calculate_age()} years old!") #this could use some work right now.....


    #after imports
    def calculate_age(self):
        # todays date and their birthday is needed!
        today = dt.datetime.today()
        bday = self.birthday.split("-")
        bday_year = int(bday[0])
        bday_month = int(bday[1])
        bday_day = int(bday[2])
        age = today.year - bday_year - ((today.month,today.day) <(bday_month, bday_day))
        return age


#create instance of students!

alice = Student("Alice","1998-10-10",'Computer Science')

print(alice.birthday)
print(alice.name)


bob = Student("Bob", "1990-05-10", "Engineering")

print(bob.name)
print(bob.birthday)

bob.study()
alice.study()
bob.celebrate_birthday()
bob.stop_studying()

bob.birthday = "1990-08-12"

print(bob.birthday)

mary = Student("mary", "1996-03-26","Art History")

mary.celebrate_birthday()


say_hello(bob.name)
