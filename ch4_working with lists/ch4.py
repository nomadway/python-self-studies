######******CHAPTER-4*******############

#LOOPing through an entire list
'''cooks = ["john", "lee", "wang"]
for cooker in cooks:
	print(cooker)'''

#Doing More Work Within a for Loop
cooks = ["john", "lee", "wang"]
for cooker in cooks:
	print(f"{cooker.title()}, the meal was delicious!")
	print(f"We would love to try your other dishes, {cooker.title()}.\n")

#Doing Something After a for Loop

print("Thank you everyone. The dinner was great.") #not indented line. prints only ONCE outside FOR loop. If indented inside LOOP, will be repeated.


##****EXERCISE 4-1***###
pizzas = ['mexican', 'margarita', 'chilli', 'super']
for pizza in pizzas:
	#print(pizza)
	print(f"I love {pizza.title()} pizza.")
	print(f"All {pizza.title()} pizzas are incredible and tasty.\n")
print(f"I just LOVE Pizzas!!!\n") 

##****EXERCISE 4-2***###
animals = ["whales", "elephants", "rhinos"]
for animal in animals:
	#print(animal)
	print(f"The population of {animal.title()} is on rapid decline.")
	print(f"{animal.title()} face extinction without international copperation.\n")
print(f"Every person, every country can help save these animals.\n")



#####****MAKING NUMERICAL LISTS******######
#Using the range() Function
for value in range(1, 11):
	print(value)

#Using range() to Make a List of Numbers
numbers = list(range(1, 11))
print(numbers)

#Generating EVEN numbers from a list
even_num = list(range(2, 16, 2))
print(even_num)

#How to SQUARE 10 numbers
square1 = []
for value in range(1, 11):
	square2 = value ** 2
	square1.append(square2)
print(square1)


#SHORTER version of SQUARE
square1 = []
for value in range(1, 5):       #the last number 5 is not calculated. Only 1,2,3,4.
	square1.append(value**2)
print(square1)















