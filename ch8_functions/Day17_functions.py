
# def select_car():
# 	print("Lexus LX 560")

# select_car()


####Passing information to FUNCTION#####

# def greeting(name):
# 	print(f"Hello, {name.title()}!")

# greeting("Mary")

####ARGUMENTS and PARAMETERS####

##EXERCISE###
# 8-1. Message: Write a function called display_message() that prints one sen-
# tence telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

# def display_message(name):
# 	print(f"Hello everyone. {name.title()} is learning python.")
# display_message("John")


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title . The function should print a message, such as One of my
# favorite books is Alice in Wonderland . Call the function, making sure to
# include a book title as an argument in the function call.

# def fav_book(title):
# 	print(f"One of my favourite books is {title.title()}.")
# fav_book("harry potter")


####POSITIONAL ARGUMENTS#####

# def pet_describe(animal_type, animal_name):
# 	print(f"\nI have a beautiful {animal_type}.")
# 	print(f"\nMy {animal_type}'s name is {animal_name.title()}.")

# pet_describe("horse", "johny")


#####KEYWORD ARGUMENTS#### A keyword argument is a name-value pair that you pass to a function.
# def pet_describe(animal_type, animal_name):
# 	print(f"\nI have a beautiful {animal_type}.")
# 	print(f"\nMy {animal_type}'s name is {animal_name.title()}.")

# pet_describe(animal_type ="horse", animal_name="johny")


#####EXERCISE#####
# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

# def make_shirt(size, message):
# 	print(f"The shirt is {size} with a message '{message.title()}'.")

# make_shirt("large", "i love osh")
# make_shirt(size="large", message="i love osh")


#####RETURNING A SIMPLE VALUE######
# def formatted_name (name, surname):
# 	full_name = f"{name} {surname}"
# 	return full_name.title()

# sportsman = formatted_name(name ="john", surname="lee")
# print(sportsman)


#####RETURNING A DICTIONARY#####

# def build_person(name, surname):
# 	person = {"first": name, "second": surname}
# 	return person

# sportsman = build_person("jimmy", "carter")
# print(sportsman)



#####Using a Function with a WHILE Loop#####

 # def formatted_name (name, surname):
	# full_name = f"{name} {surname}"
	# return full_name.title()

# while True: 

# 	print("\nPlease enter your name: ")
# 	f_name = input("First name: ")
# 	l_name = input("Last name: ")

# 	# for_name = formatted_name(f_name, l_name)
# 	print(f"\nHello {f_name} {l_name}!")


##### PASSING A LIST #######

# def greet_users(names):
# 	for name in names:
# 		message = f"Hello, {name.title()}!"
# 		print(message)

# usernames = ["John", "King", "Steve"]
# greet_users(usernames)


#####Passing an Arbitrary Number of Arguments

# def pizza_type(*toppings):
# 	print("\nMaking a pizza with the following toppings: ")
# 	for topping in toppings:
# 		print(f"- {topping}")

# pizza_type("cheese", "tomato")
# pizza_type("salami", "olive", "apple")



#######Mixing Positional and Arbitrary Arguments######

# def pizza_type(size, *toppings):
# 	print(f"\nMaking a {size} inch pizza with the following toppings: ")
# 	for topping in toppings:
# 		print(f"- {topping}")

# pizza_type(25, "cheese", "tomato")
# pizza_type(45, "salami", "olive", "apple")


###
































