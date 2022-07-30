# #9-1
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name=restaurant_name
#         self.type=cuisine_type
#     def describe_restaurant(self):
#         print(self.name)
#         print(self.type)
#     def open_restaurant(self):
#         print(self.name+" is open")
# my_restaurant=Restaurant('KFC','chicken')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
#
# #9-2
# my_restaurant=Restaurant('KFC','chicken')
# my_restaurant.describe_restaurant()
# my_restaurant=Restaurant('mcdonald','hamburger')
# my_restaurant.describe_restaurant()
# my_restaurant=Restaurant('burger king','drumsticks')
# my_restaurant.describe_restaurant()
#
# #9-3
# class User():
#     def __init__(self,first_name,last_name,age,gender):
#         self.fname=first_name
#         self.lname=last_name
#         self.a=age
#         self.g=gender
#     def describe_user(self):
#         print(self.fname)
#         print(self.lname)
#         print(self.a)
#         print(self.g)
#     def greet_user(self):
#         print('Hello '+self.fname)
# user1=User('bruce','weien',23,'man')
# user1.describe_user()
# user1.greet_user()

# #9-4
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name=restaurant_name
#         self.type=cuisine_type
#         self.number=0
#     def describe_restaurant(self):
#         print(self.name)
#         print(self.type)
#     def open_restaurant(self):
#         print(self.name+" is open")
#     def number_served(self):
#         print('The are '+str(self.number)+' people have dinner here')
# my_restaurant=Restaurant('mcdonald','hamburger')
# my_restaurant.number_served()
# my_restaurant.number=1
# my_restaurant.number_served()
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name=restaurant_name
#         self.type=cuisine_type
#         self.number=0
#     def describe_restaurant(self):
#         print(self.name)
#         print(self.type)
#     def open_restaurant(self):
#         print(self.name+" is open")
#     def number_served(self):
#         print('The are '+str(self.number)+' people have dinner here')
#     def set_number_served(self,num):
#         self.number=num
# my_restaurant=Restaurant('mcdonald','hamburger')
# my_restaurant.number_served()
# my_restaurant.set_number_served(20)
# my_restaurant.number_served()
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name=restaurant_name
#         self.type=cuisine_type
#         self.number=0
#     def describe_restaurant(self):
#         print(self.name)
#         print(self.type)
#     def open_restaurant(self):
#         print(self.name+" is open")
#     def number_served(self):
#         print('The are '+str(self.number)+' people have dinner here')
#     def set_number_served(self,num):
#         self.number=num
#     def increment_number_served(self,nums):
#         self.number+=nums
# my_restaurant = Restaurant('mcdonald', 'hamburger')
# my_restaurant.number_served()
# my_restaurant.set_number_served(20)
# my_restaurant.increment_number_served(20)
# my_restaurant.number_served()
#
# #9-5
# class User():
#     def __init__(self,first_name,last_name,age,gender,login_attempets):
#         self.fname=first_name
#         self.lname=last_name
#         self.a=age
#         self.g=gender
#         self.l=login_attempets
#     def describe_user(self):
#         print(self.fname)
#         print(self.lname)
#         print(self.a)
#         print(self.g)
#         print(self.l)
#     def greet_user(self):
#         print('Hello '+self.fname)
#     def increment_login_attempts(self):
#         self.l+=1
#     def reset_login_attempts(self):
#         self.l=0
# user1=User('bruce','weien',23,'man',0)
# user1.increment_login_attempts()
# user1.describe_user()
# user1.increment_login_attempts()
# user1.describe_user()
# user1.increment_login_attempts()
# user1.describe_user()
# user1.reset_login_attempts()
# print(str(user1.l))

# #9-6
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name=restaurant_name
#         self.type=cuisine_type
#     def describe_restaurant(self):
#         print(self.name)
#         print(self.type)
#     def open_restaurant(self):
#         print(self.name+" is open")
# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors=['strawberry flavor','chocolate flavor','apple flavor']
#     def show_flavor(self):
#         print("\nWe have the following flavors available:")
#         for flavor in self.flavors:
#             print("- " + flavor.title())
# ice=IceCreamStand('Haagen-Dazs','ice')
# ice.show_flavor()
#
# #9-7
# class User():
#
#     def __init__(self, first_name, last_name, username, email, location):
#         # 初始化用户
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#
#     def describe_user(self):
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         print("\nWelcome back, " + self.username + "!")
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, username, email, location):
#         super().__init__(first_name, last_name, username, email, location)
#         self.privileges = []
#
#     def show_privileges(self):
#         for privilege in self.privileges:
#             print("- " + privilege)
#
#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
#
# eric.privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
# ]
#
# eric.show_privileges()

# #9-8
# class User():
#
#     def __init__(self, first_name, last_name, username, email, location):
#         # 初始化用户
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#
#     def describe_user(self):
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         print("\nWelcome back, " + self.username + "!")
#
# class Privileges():
#
#     def __init__(self, privileges=[]):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print("\nPrivileges:")
#         if self.privileges:
#             for privilege in self.privileges:
#                 print("- " + privilege)
#         else:
#             print("- This user has no privileges.")
#
# class Admin(User):
#     def __init__(self, first_name, last_name, username, email, location):
#         super().__init__(first_name, last_name, username, email, location)
#         self.privileges =Privileges()
#
#     def show_privileges(self):
#         for privilege in self.privileges:
#             print("- " + privilege)
#
#
#
#
#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
#
# eric.privileges.show_privileges()
#
# print("\nAdding privileges...")
# eric_privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
# ]
# eric.privileges.privileges = eric_privileges
# eric.privileges.show_privileges()
#
# #9-9
# class Car():
#
#     def __init__(self, manufacturer, model, year):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery():
#
#     def __init__(self, battery_size=60):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         if self.battery_size == 60:
#             range = 140
#         elif self.battery_size == 85:
#             range = 185
#
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#     def upgrade_battery(self):
#         if self.battery_size == 60:
#             self.battery_size = 85
#             print("Upgraded the battery to 85 kWh.")
#         else:
#             print("The battery is already upgraded.")
#
#
# class ElectricCar(Car):
#
#     def __init__(self, manufacturer, model, year):
#         super().__init__(manufacturer, model, year)
#         self.battery = Battery()
#
#
# print("Make an electric car, and check the battery:")
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# my_tesla.battery.describe_battery()
#
# print("\nUpgrade the battery, and check it again:")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
#
# print("\nTry upgrading the battery a second time.")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()

# #9-10
# from restaurant import Restaurant
# channel_club = Restaurant('the channel club', 'steak and seafood')
# channel_club.describe_restaurant()
# channel_club.open_restaurant()
#
# #9-11
# from user import Admin
#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
#
# eric_privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
#     ]
# eric.privileges.privileges = eric_privileges
#
# print("\nThe admin " + eric.username + " has these privileges: ")
# eric.privileges.show_privileges()

# #9-12
# from admin import Admin
#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
#
# eric_privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
#     ]
# eric.privileges.privileges = eric_privileges
#
# print("\nThe admin " + eric.username + " has these privileges: ")
# eric.privileges.show_privileges()

# #9-13
# from collections import OrderedDict
# glossary = OrderedDict()
# glossary['string'] = 'A series of characters.'
# glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
# glossary['list'] = 'A collection of items in a particular order.'
# glossary['loop'] = 'Work through a collection of items, one at a time.'
# glossary['dictionary'] = "A collection of key-value pairs."
# glossary['key'] = 'The first item in a key-value pair in a dictionary.'
# glossary['value'] = 'An item associated with a key in a dictionary.'
# glossary['conditional test'] = 'A comparison between two values.'
# glossary['float'] = 'A numerical value with a decimal component.'
# glossary['boolean expression'] = 'An expression that evaluates to True or False.'
# for word, definition in glossary.items():
#     print("\n" + word.title() + ": " + definition)
#
# #9-14
# from random import randint
#
# class Die():
#     """Represent a die, which can be rolled."""
#
#     def __init__(self, sides=6):
#         """Initialize the die."""
#         self.sides = sides
#
#     def roll_die(self):
#         """Return a number between 1 and the number of sides."""
#         return randint(1, self.sides)
#
# d6 = Die()
#
# results = []
# for roll_num in range(10):
#     result = d6.roll_die()
#     results.append(result)
# print("10 rolls of a 6-sided die:")
# print(results)
#
# d10 = Die(sides=10)
#
# results = []
# for roll_num in range(10):
#     result = d10.roll_die()
#     results.append(result)
# print("\n10 rolls of a 10-sided die:")
# print(results)
#
# d20 = Die(sides=20)
#
# results = []
# for roll_num in range(10):
#     result = d20.roll_die()
#     results.append(result)
# print("\n10 rolls of a 20-sided die:")
# print(results)
