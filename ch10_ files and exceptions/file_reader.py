
###CHAPTER-10  FILES AND EXCEPTIONS 


###OPENS FILE IN ABSOLUTE PATH, THAT'S CONCRETE AND SPECIFIC DIRECTORY AND FOLDER 

# file_path = '/home/buranidze/Documents/python_crash_ course/ch10_ files and exceptions/p_digits.txt'
# with open(file_path) as file_object:
# 	contents = file_object.read()
# print(contents)


###OPENS THE FILE WHEN BOTH .PY AND .TXT ARE IN THE SAME FOLDER 

# with open('p_digits.txt') as file_object:
# 	contents = file_object.read()
# print(contents)


####READING LINE BY LINE

# file_name = "p_digits.txt"
# with open ("p_digits.txt") as file_object:
# 	for line in file_object:
# 		print(line)


#####WORKING WITH A FILE'S CONTENTS***####

# file_name = "p_digits.txt"
# with open ("p_digits.txt") as file_object:
# 	lines = file_object.readlines()

# pi_string = ""
# for line in lines:
# 	pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))


##LARGE FILES - ONE MILLION DIGITS

# file_name = "pi_million_digits.txt"

# with open("pi_million_digits.txt") as file_object:
# 	lines = file_object.readlines()

# pi_string = ""
# for line in lines:
# 	pi_string += line.strip()

# print(f"{pi_string[:10]}")
# print(len(pi_string))

####IS YOUR BIRTHDAY CONTAINED IN PI?

# file_name = "pi_million_digits.txt"

# with open("pi_million_digits.txt") as file_object:
# 	lines = file_object.readlines()

# pi_string = ""
# for line in lines:
# 	pi_string += line.strip()

# birthday = input("Enter your birthday in the form ddmmyyyy: ")
# if birthday in pi_string:
# 	print("Your birthday appears in the first 300 digits.")

# else:
# 	print("Your birthday does not appear in the first 300 digits.")


####EXERCISE####
# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt in
# the same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by stor-
# ing the lines in a list and then working with them outside the with block.

##step 1 Write a program that reads the file and prints what you wrote three times.
# with open('learning_python.txt') as file_object:
# 	contents = file_object.read()
# print(contents)

###STEP 2 
# file_name = "learning_python.txt"
# with open(file_name) as file_object:
# 	for line in file_object:
# 		print(line)

##Step 3
# file_name = "learning_python.txt"
# with open (file_name) as file_object:
# 	lines = file_object.readlines()

# pi_string = []
# for line in lines:
# 	pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))


##WRITING TO AN  EMPTY FILE
# file_name = "programming.txt"
# with open(file_name, "w") as file_object:
# 	file_object.write("I love coding in Python!\nPython is the most popular language!")

##WRITING MULTIPLE LINES
# file_name = "programming.txt"
# with open(file_name, "w") as file_object:
# 	file_object.write("Hello Mars!")
# 	file_object.write("This is Earth calling.")
# 	file_object.write("Please respond to our messages.")

###APPENDING TO A FILE
# file_name = "programming.txt"
# with open(file_name, "a") as file_object:
# 	file_object.write("\nI also love using Python for analysing large data.") 
# 	file_object.write("\nIn addition, I would like to use Python in Cyber Security.")


##EXERCISE########
# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

# name = input("Please enter your full name: ")

# file_name = "guest.txt"
# with open(file_name, "w") as file_object:
# 	file_object.write(name)


# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

# file_name = "guest_book.txt"

# print("Enter 'quit' when you are finished.")

# while True:
# 	name = input("\nEnter your full name: ")
# 	if name == "quit":
# 		break
# 	else: 
# 		with open(file_name, "a") as new_names:
# 			new_names.write(name + "\n") ##\n adds each new name to a seperate new line
# 		print("Hello " + name+ ", you've been added to the guest book!")


# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

##VERSION-1 (simple)

# file_name = "like_programming.txt"

# while True:
# 		ask = input("\nWhy do you like programming? ")

# 		with open(file_name, "a") as responses:
# 			responses.write(ask + "\n")

##VERSION-2

# file_name = "like_programming.txt"

# responses = []

# while True:
# 	ask1 = input("\nDo you like programming? ")
# 	responses.append(ask1)

# 	ask2 = input("Would you want others to respond? (y/n) ")
# 	if ask2 != "y":
# 		break

# with open (file_name, "a") as answers:
# 	for ask1 in responses:
# 		answers.write(ask1 + "\n")










































