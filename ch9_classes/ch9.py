
#####************CLASSES***************************

# class Dog:

# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age 

# 	def sit (self):
# 		print(f"{self.name} is now sitting.")

# 	def jump(self):
# 		print(f"{self.name} likes jumping and playing.")


# my_dog = Dog("Bim", 5)   ##my_dog is a FIRST instance 
# my_dog.sit()
# my_dog.jump()

# print(f"My dog's name is {my_dog.name}.")
# print(f"{my_dog.name} is {my_dog.age} years old.")

# my_friends_dog = Dog("Rex", 3)  #my_friends_dog is a SECOND instance 
# print(f"\nMy friend dog's name is {my_friends_dog.name}.")
# print(f"{my_friends_dog.name} is {my_friends_dog.age} years old.")
# my_friends_dog.sit()

####*******EXERCISE*****************#######
# 9-1. Restaurant: Make a class called Restaurant . The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type .
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

# class Restaurant:

# 	def __init__(self, restaurant_name, cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		print(f"\n{self.restaurant_name} is a new restaurant that serves delicious {self.cuisine_type} food.")

# 	def open_restaurant(self):
# 		print(f"\n{self.restaurant_name} is open from Monday to Saturday.")

# my_restaurant = Restaurant("SKY", "Lebanese")
# print(my_restaurant.restaurant_name)
# print(my_restaurant.cuisine_type)

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

# class Restaurant:

# 	def __init__(self, restaurant_name, cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		print(f"\n{self.restaurant_name} is a new restaurant that serves delicious {self.cuisine_type} food.")

# leban = Restaurant("SKY", "Lebanese")  #Instance 1
# leban.describe_restaurant()

# china = Restaurant("OCEAN", "Chinese") #Instance 2
# china.describe_restaurant()

# eng = Restaurant("KING'S", "English") #Instance 3
# eng.describe_restaurant()


# 9-3. Users: Make a class called User . Create two attributes called first_name
# and last_name , and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

# class User:

# 	def __init__(self, name, surname, age, citizenship):
# 		self.name = name
# 		self.surname = surname
# 		self.age = age
# 		self.citizenship = citizenship

# 	def describe_user(self):
# 		print(f"\n{self.name} {self.surname} is {self.age} years old. He is {self.citizenship}.")

# 	def greet_user(self):
# 		print(f"Hello {self.name} {self.surname}. How are you today?")

# user1 = User("John", "Lee", 34, "British")
# user1.describe_user()
# user1.greet_user()

# user2 = User("Boris", "Aleksandrovich", 45, "Russian")
# user2.describe_user()
# user2.greet_user()

# user3 = User("Jack", "Ma", 37, "Chinese")
# user3.describe_user()
# user3.greet_user()
