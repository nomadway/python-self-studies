######**********CHAPTER-5*****###########
# super_cars = ["bentley", "ferrari", "nissan"]
# for car in super_cars:
# 	if car == "ferrari":
# 		print(car.upper())
# 	else:
# 		print(car.title())


###**CHECKING FOR INEQUALITY*****#####
# chocolate = "snickers"
# if chocolate != "twix":
# 	print("Snickers is awesome!")


###COMPARING NUMBERS##
# age = 16
# if age != 18:
# 	print("You are not allowed to enter this site.")

###CHEKING IF THE VALUE IS IN THE LIST
# toppings = ["apple", "berry", "cherry"]
# if "apple" in toppings:
# 	print('True')
# else:
# 	print("false")


#####CHECKING WHETHER A Value Is Not in a List######

# people_list = ["steve", "susan", "kevin"]
# user = "mary"
# if user not in people_list:
# 	print(f"{user.title()} You can add your comments here.")

#####  IF STATEMENTS  #######
# age = 20
# if age >= 20:
# 	print("You are allowed to cast a vote.")

####  IF ESLE STATEMENTS #####

# age = 16
# if age >= 18:
# 	print("You are allowed to cast a vote.")
# else:
# 	print("Sorry, you are not old enough to vote this year.")

####### IF   ELIF   ELSE ############
# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $25.
# Admission for anyone age 18 or older is $40.

# age = 10
# if age < 4:
# 	print("Free Admission.")

# elif age < 18:
# 	print("Admission fee is $25.")

# elif age > 20:
# 	print("Fee is $15.")

# else:
# 	print("Admissio fee is $40.")

########## TESTING MULTIPLE CONDITIONS #######
# toppings = ["apple", "berry", "cherry", "lemon"]

# if "apple" in toppings:
# 	print("Add apple.")
# if "berry" in toppings:
# 	print("Adding berry")
# if "grape" in toppings:
# 	print("Adding grape")

# print("\nFinished making pizza.")

##### USING IF WITH LISTS ###########
# toppings = ["apple", "berry", "cherry", "lemon"]
# for topping in toppings:
# 	if topping == "berry": 
# 		print("Sorry, we are out of berry at the moment.")

# else: 
# 	print(f"Adding fresh {topping}") 

# print("\nFinished making pizza.")

#######USING MULTIPLE LISTS ####
toppings = ["apple", "berry", "cherry", "lemon"]

requested_top = ["apple", "chocolate", "cherry"]

for requested_t in requested_top:
	if requested_t in toppings:
		print(f"Adding {requested_t}")

	else: 
		print(f"Sorry, we don't have {requested_t}")




