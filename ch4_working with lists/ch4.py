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

#EVEN SHORTER version of SQUARE
square5 = [value**2 for value in range(1, 11)]
print(square5)


#Simple Statistics with a List of Numbers
numbers = [1,2,0,-1,3,4,5,-7,6,7,9,8,10,11]
print (min(numbers))
print(max(numbers))
print(sum(numbers))

#######**********EXERCISES**********##########
#4-3. Counting to Twenty: Use a FOR loop to print the numbers from 1 to 20,inclusive.
for value in range(1, 21):
	print(value)

'''#4-4 Make a list from 1 to million and print the numbers using FOR loop
onemillion = range(1, 1000001)
for million in onemillion:
	print(million)'''

'''#4-5. Summing a Million: Make a list of the numbers from one to one million,
#and then use min() and max() to make sure your list actually starts at one and
#ends at one million. Also, use the sum() function to see how quickly Python can
#add a million numbers.
millions = range(1, 1000001)
print(min(millions))
print(max(millions))
print(sum(millions))'''

#4-6. Odd Numbers: Use the third argument of the range() function to make a
#list of the odd numbers from 1 to 20. Use a for loop to print each number.
##**ODD VERSION-1*****
od_num = list(range(1, 20))
for od in od_num:
	if od % 2 != 0:
		print(od)

#***ODD VERSION-2****
odd_n = list(range(1, 20, 2))   #if the first digit is 1, and the third digit is 2, ODD numbers will be printed.
print(odd_n)


'''##EVEN Number, VERSION-1                   
even_nummm = list(range(2, 16, 2))
print(even_nummm)'''                #######printuet LIST

'''##EVEN Number, VERSION-2
even_no = list(range(2, 24))
for even in even_no:
	if even % 2 == 0:
		print(even)'''              ######printuet VERTIKAL'NO 


#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
#VERSION-1
'''list_mult = list(range(3, 29, 3))     #prints in LIST 
print(list_mult)'''

#VERSION-2                               ALSO A GOOD VERSION, prints in VERTICAL 
for value1 in list(range(3, 34, 3)):
	print(value1)

#VERSION-3 /////                          BEST VERSION    TO FIND MULTIPLES OF 3  
list_mult1 = list(range(3, 31))
#print(list_mult1)
for mult in list_mult1:
	if mult % 3 == 0:
		print(mult)

#4-8. Cubes: A number raised to the third power is called a cube. For example,
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube.

#VERSION-1     CUBE 
cubes = []
for value in range(1, 11):       
	cubes.append(value**3)
print(cubes)

#VERSION-2 CUBE   SHORTER VERSION 
cubes1 = [value**3 for value in range(1, 6)]
print(cubes1)


#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes10 = [value**3 for value in range(1, 11)]
print(cubes10)


###*********SLICING A LIST***********#############

soft_drinks = ['coke', 'fanta', 'sprite', 'lemonade', 'juice']
print(soft_drinks[0:3]) #it will print coke, fanta, sprite


soft_drinks1 = ['coke', 'fanta', 'sprite', 'lemonade', 'juice']
print(soft_drinks[:4]) # it will print coke,fanta, sprite, lemonade.

soft_drinks2 = ['coke', 'fanta', 'sprite', 'lemonade', 'juice']
print(soft_drinks[2:]) # it will print sprite, lemonade, juice

soft_drinks3 = ['coke', 'fanta', 'sprite', 'lemonade', 'juice']
print(soft_drinks[-3:]) # it will print the LAST THREE - sprite, lemonade, juice

###*********LOOPING THROUGH A SLICE***********#############
cities = ["tokyo","london", "singapore", "geneva", "toronto"]
print("This is the list of three cities:")
for city in cities[:3]:
	print(city.title())
