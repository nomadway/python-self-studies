
##CH-7   INPUT function   AND WHILE LOOP 

# message = input("Hello Marry! Enter your age please: ")
# print(message)

# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# prompt = "If you define the date, we can then plan the dinner."
# prompt += "\nWhat is your name? "
# name = input(prompt)
# print(f"\nHello, {name.title()}!")

##########************Using int() to Accept Numerical Input******####

# age = input("What is your age? ")
# print(age)

#example
# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
# 	print("\nYou are old enough to enter the club")
# else: 
# 	print("\nYou are underage to enter the premises.")

#####THE MODULO OPERATOR 
# number = input("Enter the number: ")
# number = int(number)

# if number % 2 == 0:
# 	print(f"\n The number {number} is even.")

# else:
# 	print(f"\nThe number {number} is odd.")


####EXERCISE####
# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

# car_rental = input("What kind of car would you like? ")
# print(f"\nLet me check if we have {car_rental} in stock.")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

# people = input("How many people are in your dinner group? ")
# people = int(people)

# if people > 8:
# 	print("\n I am afraid you will need to wait for a table.")
# else:
# 	print("\nTable for your dinner group is ready.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

# number = input("Enter a number: ")
# number = int(number)

# if number % 2 == 0:
# 	print(f"The number {number} is a multiple of 10.")
# else:
# 	print(f"The number {number} is not a multiple of 10")


#####****WHILE LOOP****#######

# number = 1
# while number <= 10:    #counting stops at 10
# 	print(number)
# 	number += 1

# number = 2
# while number <= 10:
# 	print(number) 
# 	number +=1    #counts from 2 to 10

# num = 1
# while num < 10:
# 	print(num)
# 	num += 1      #counts from 1 to 9 

# Letting the User Choose When to Quit

# prompt = "\nLet me tell you something."
# prompt += "\nEnter 'quit' to end the game: "

# message = ""
# while message != "quit":
# 	message = input(prompt)
# 	if message != "quit":  ####we can use IF to hide the word QUIT from being printed. 
# 		print(message)

###USING A FLAG 
# flag, acts as a signal to the program. We
# can write our programs so they run while the flag is set to True and stop run-
# ning when any of several events sets the value of the flag to False .

#FLAG can be assigned any name..e.g. active, on,....

# prompt = "\nLet me tell you something:"
# prompt = "\nEnter ''quit to end the game."

# active = True
# while active:
# 	message = input(prompt)

# 	if message == "quit":
# 		active = False 

# 	else:
# 		print(message)


###Using break to Exit a Loop

# prompt = ("\nEnter a name of the planet you would like to visit:")
# prompt += "\n(Enter 'quit' to exit.)"

# while True:
# 	planet = input(prompt)

# 	if planet == "quit":

# 		break
# 	else:
# 		print(f"\nI'd like to visit {planet.title()}.")	

#####Using continue in a Loop######

# number = 0
# while number < 10:
# 	number += 1
# 	if number % 2 == 0:

# 		continue 
		
# 	print(number)


#####Avoiding Infinite Loops

# a = 1
# while a <= 10:
# 	print(a)
# 	a += 1


###EXERCISE
# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.	

# prompt = ("\nEnter your choice of pizza toppings: ")
# prompt += "\n(Enter 'quit' to end your topping selection.)"

# while True:
# 	topping = input(prompt)

# 	if topping == "quit":

# 		break
# 	else:
# 		print(f"\nYour{topping.title()} will be added to your pizza.")	


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket


age = 2
if age < 3:
	print(Free entry for under 3 year olds.")


	# if age > 3 and age >12:
	# 	print("\nThe ticket is $10.")

elif age > 12:
		print("\nTicket is $15.")

else:
	print("fee is $10")



