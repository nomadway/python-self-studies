######CHAPTER-3####################
#*---LISTS----#
cars = ["lexus", "toyota", "bentley", "tesla"]
print(cars)

#Accessing Elements in a list#
print(cars[0]) #prints the first car in the list

print(cars[0].title()) #print the cars with Capital letter

print(cars[-1]) #prints the last car 

message = f"My first car was {cars[1].title()}." #using individual values with {}
print(message)

#EXERCISE#
names = ["Aidana!", "Aigerim!", "Begimay!", "Saltanat!"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])

greeting0 = f"Hello, {names[0]}"
print(greeting0)  
greeting1 = f"Hello, {names[1]}"
print(greeting1)
greeting2 = f"Hello, {names[2]}"
print(greeting2)
greeting3 = f"Hello, {names[3]}"
print(greeting3)


cash = ["billion", "million", "trillion"]
message = f"I have {cash[0].title()} Dollars."
print(message)

#CHANGING, ADDING and REMOVING ELEMENTS
#*Moodifying elements in a list*#

cars = ["lexus", "toyota", "bentley", "tesla"]
print(cars)

cars[0] = "mercedes"
print(cars)

#*Adding elements to a list* by using .append method. New item will be added to the end of the list.
cars = ["lexus", "toyota", "bentley", "tesla"]
print(cars)
cars.append("ferrari")
print(cars)

#Adding elements to an emply list
food = []
print(food)

food.append("plov")
food.append("kebab")
food.append("beshmarmak")
print(food)

#Adding a new element at any position
cars = ["lexus", "toyota", "bentley", "tesla"]
cars.insert(0, "lamborghini")
print(cars)

#Removing elements from a list
food = ["plov", "kuurdak", "manty", "shashlyk"]
print(food)

del food [3]
print(food)


#Removing elements using .pop() method
#The pop() method removes the last item in a list, but it lets you work with that item after removing it.
cars = ["lexus", "tesla", "bentley", "toyota"]
print(cars.pop()) #vytaskivaet tol'ko tesla v terminal

cars = ["lexus", "tesla", "bentley", "toyota"]
first_owned = cars.pop()
print(f"The first car I owned was a {first_owned.title()}.")


#Popping Items from any Position in a List
food = ["plov", "kuurdak", "manty", "shashlyk"]
print(food.pop(0))


food = ["plov", "kuurdak", "manty", "shashlyk"]
fav_food = food.pop(0)
print(f"My favourite food is {fav_food.title()}!")

#Removing an Item by Value
cars = ["lexus", "tesla", "bentley", "toyota"]
print(cars)

cars.remove("toyota")
print(cars)

food = ["plov", "kuurdak", "manty", "shashlyk"]
too_fatty = "kuurdak"
food.remove(too_fatty)
print(f"{too_fatty.title()} is too heavy for me!")

#Chapter-3 EXERCISE 

#Step-1 Create a Guest List
guest = ["Buffet", "Jobs", "Bezzos"]

#Step-2 Print their names and Greet each person
print(guest)
print(guest[0])
print(guest[1])
print(guest[2])

greeting0 = f"Hello, {guest[0]}! Come to dinner today at 18:45pm."
print(greeting0)  
greeting1 = f"Hello, {guest[1]}! Come to dinner today at 18:45pm."
print(greeting1)
greeting2 = f"Hello, {guest[2]}! Come to dinner today at 18:45pm."
print(greeting2)

#Step-3 Changing guest list. Remove one person from the list who cannot come to dinner
guest = ["Buffet", "Jobs", "Bezzos", "Mask","Zuckerberg"]
print(guest)

del guest [4]
print(guest)

guest.remove("Mask")
print(guest)

#Step-4 Add the new guest to the list
guest.append("Lee") #adds the name to the last position in the list
print(guest)

guest.insert(0, "lee".title()) #adds the name to the front position with Capital L letter.
print(guest)

#Step-5 Print the New guest list with greeting
print(guest[0]) #Lee
print(guest[1]) #Buffet
print(guest[2]) #Jobs
print(guest[3]) #Bezzos
print(guest[4]) #Mask

greeting0 = f"Hello, {guest[0]}! Come to dinner today at 18:45pm."
print(greeting0)  
greeting1 = f"Hello, {guest[1]}! Come to dinner today at 18:45pm."
print(greeting1)
greeting2 = f"Hello, {guest[2]}! Come to dinner today at 18:45pm."
print(greeting2)
greeting3 = f"Hello, {guest[3]}! Come to dinner today at 18:45pm."
print(greeting3)
greeting4 = f"Hello, {guest[4]}! Come to dinner today at 18:45pm."
print(greeting4)


#Add more guests to the list 
#Step-1 Inform guests about the new venue
print(f" Dear {guest[0]}, {guest[1]}, and {guest[2]}: this is to infrom you that the event will take place at Plaza hotel.")

#Step-2 Add one new name to the list
name1 = ["Buffet", "Jobs", "Bezzos", "Mask","Zuckerberg"]
name1[0] = "Putin"
print(name1)

name2 = ["Buffet", "Jobs", "Bezzos", "Mask","Zuckerberg"]
name2.insert(0, "Mao")
print(name2)

name3 = ["Buffet", "Jobs", "Bezzos", "Mask","Zuckerberg"] #[] will replace existing name with new name
name3[2] = "Putin"
print(name3)

name4 = ["Buffet", "Jobs", "Bezzos", "Mask","Zuckerberg"]
name4.append("Putin")
print(name4)

name5 = ["Buffet", "Jobs", "Bezzos", "Mask","Zuckerberg"] #.insert() add the new name to the list. 
name5.insert(5, "Putin")
print(name5)

##############EXERCISE 3-7#################
#Step-1 Inform guests that only TWO can be invited to dinner
name1 = ["Putin", "Nazarbaev", "Aliev", "Lukashenko"]
print(name1)

print(name1[0])
print(name1[1])
print(name1[2])
print(name1[3])

message = f"Hello {name1[0]}! {name1[1]}! {name1[2]}! and {name1[3]}!: please be informed that only two guests are invited to dinner."
print(message)


#Step-2 Delete quests one by one until only two are left. Each time one is deleted, message them that you are sorry.
name11 = ["Putin", "Nazarbaev", "Aliev", "Lukashenko"]
delete1 = name1.pop(1)
print(name11)
print(f"Dear Mr {delete1}! We are sorry for being unable to host you to dinner tonight.")

delete2 = name11.pop(2)
print(name1)
print(f"Dear Mr {delete2}! We are sorry for being unable to host you to dinner tonight.")

name2 = ["Putin", "Lukashenko"]
print(f"Dear Mr {name2[0]}! We are glad to have you for dinner.")
print(f"Dear Mr {name2[1]}! We are glad to have you for dinner.") 

#Step-3 Delete the last two names from the list. The list should be empty. 

name2 = ["Putin", "Lukashenko"]
print(name2)

del name2[0]
del name2[0]
print(name2)




#####********ORGANIZING A LIST****************#############

#Sorting a List PERMANENTLY with the SORT() Method, ALPHABETICALLY

cars = ['tesla', 'lexus', 'bentley', 'ferrari']
cars.sort()
print(cars) #The cars are now in alphabetical order, and we can never revert to the original order. 

#Sorting list in reverse alphabetical order
laptops = ['apple', 'huawei', 'hp', 'acer']
laptops.sort(reverse=True)
print(laptops)

#Sorting a List TEMPORARILY with the SORTED() Method, ALPHABETICALLY
car = ['tesla', 'lexus', 'bentley', 'ferrari']
print('\nHere is the original list of cars:')
print(car)

print('\nHere is the sorted list of cars:')
print(sorted(car))

print('\nHere is the original list of cars again:')
print(car)

print("\nHere is the SORTED REVERSE list of cars:")       #	SORTED in REVERSE order 
car5 = ['teslas', 'lexusss', 'bentleyyy', 'ferrariii']
print(sorted(car5, reverse=True))


####Printing a List in REVERSE Order /reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list:
print('\nHere is the list of ORIGINAL colours:')
colours = ['green', 'blue', 'white', 'dark']
print(colours)
colours.reverse()
print('\nHere is the REVERSE list of colors:')
print(colours)
'''The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time.'''
print("\nHere is the ORIGINAL List again:")
colours.reverse()
print(colours)

#######Finding the LENGHT of a List
print("\nHere is the list of cities I have lived in thus far:")
cities = ["London", "Geneva", "Singapore", "Toronto"]
print(cities)
print(len(cities))



############EXERCISE 3-8
print("\nORIGINAL list of places:")
places = ["Cuba", "Argentina", "Brazil", "Greenland", "China"]
print(places)

#Step-1 Use SORTED() to print your list in alphabetical order without modifying the actual list.
print("\nSORTED list of places:")
print(sorted(places))

#Step-2 Print the ORIGINAL List again
print("\nORIGINAL List again:")
print(places)

#Step-3 Use SORTED() to print your list in reverse alphabetical order without changing the order of the original list.
places.reverse()
print("\n REVERSED list of places")
print(places)

#Step-4 REVERSE back to the ORIGINAL List
print("\nORIGINAL list again:")
places.reverse()
print(places)

#Step-5 Use SORT() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print("\nORIGINAL list of nations:")
nations = ["Cuba", "Argentina", "Brazil", "Greenland", "China"]
print(nations)

print("\nSORT list of nations:")
nations.sort()
print(nations)

#Step-6 Use sort() to change your list so it’s stored in reverse alphabetical order.Print the list to show that its order has changed
print("\nORIGINAL list of countries:")
countries = ["Cuba", "Argentina", "Brazil", "Greenland", "China"]
print(countries)

print("\nREVERSED SORT list of countries:")
countries.sort(reverse=True)
print(countries)



























































































































