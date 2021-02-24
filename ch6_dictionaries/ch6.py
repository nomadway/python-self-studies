
#####CHAPTER 6 DICTIONARIES###########


###A SIMPLE DICTIONARY
# alien_0 = {'color': 'brown', 
# 			'points': 40}
# print(alien_0['color'])
# print(alien_0['points'])



####Accessing Values in a Dictionary
# car = {"model": "bentley", "year": 2020}
# print(car)

# car_year = car["year"]
# print(f"\nThis car was made in {car_year}.")


##ADDING ADDITIONAL KEY-VALUES
# car = {"model": "bentley", "year": 2020}
# print(car)

# car["color"] = "white"
# car["length"]= 200
# print(car)

###Starting with an Empty Dictionary
# car = {}
# car["model"]="ferrari"
# car["year"]=2021
# print(car)


###Modifying Values in a Dictionary
# car = {"model": "bentley", "year": 2020}
# print(f"This is {car['model']}.")

# car["model"]="mercedes"
# print(f"This is {car['model']}")



# lion1 = {'x_position': 0, 'y_position': 10, 'speed': 'fast'}
# print(f"Original position: {lion1['x_position']}")

# if lion1["speed"] == "slow":
# 	x_increment = 1

# elif lion1["speed"] == "medium":
# 	x_increment = 2

# else:
# 	x_increment = 3

# lion1['x_position'] = lion1['x_position'] + x_increment
# print(f"New position: {lion1['x_position']}")



####Removing Key-Value Pairs
# lion = {'color': 'green', 'points': 5}
# print("These is the original list of data.")
# print(lion)

# del lion['points']
# print("\nThis is the revised list of data.")
# print(lion)

###Looping Through All Key-Value Pairs

# user1 = {
# 	"username": "richman",
# 	"name": "John",
# 	"surname": "Lee"
# }
# print(user1)
# print("\nDetailed information about 'user1'.")

# for key, value in user1.items():
# 	print(f"\nKey: {key}")
# 	print(f"Value: {value}")

###LOOPING THROUGH ALL THE KEY-VALUE PAIRS IN DICTIONARIES
# fav_cars = {
# 	"john": "bmw",
# 	"uran": "bentley",
# 	"lee": "ferrari",
# 	"mike": "mercedes"
# }
# print(fav_cars)

# for name, car in fav_cars.items():
# 	print(f"{name.title()}'s favourite car is {car}.")

#####Looping Through All the Keys in a Dictionary
# fav_cars = {
# 	"john": "bmw",
# 	"uran": "bentley",
# 	"lee": "ferrari",
# 	"mike": "mercedes"
# }

# for name in fav_cars.keys():
# 	print(name.title())


# fav_cars = {
# 	"john": "bmw",
# 	"uran": "bentley",
# 	"lee": "ferrari",
# 	"mike": "mercedes"
# }
# if "Edward" not in fav_cars.keys():
# 	print("Erin, please join the mailing list.")


####NESTING
# car1 = {"model": "bmw", "year": 1990}
# car2 = {"model": "ferrari", "year": 2000}
# car3 = {"model": "nissan", "year": 2020}

# car = (car1, car2, car3)
# for cars in car:
# 	print(car)

###EXAMPLE
# Step-1 Create an empty list for storing cars
cars = []
#Step-2 Create 20 new cars using RANGE()
for car_number in range(20):
	new_cars = {"model":"bentley", "year": 2020, "speed": 350}
	cars.append(new_cars)
	print(cars)

#Step-3 SHow the first 10 cars
print("\nThis is the list of ten cars: ")
for car in cars[:11]:
	print(car)

print(f"Total number of cars is: {len(cars)}")

