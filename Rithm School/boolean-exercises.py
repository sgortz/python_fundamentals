# 1. Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"

# 2. Write a comment that says "This is a comment."
# This is a comment.

# 3. Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

# 4. Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."`
if 1 < 2 < 4:
    print("Math is fun.")

# 5. Assign a variable called nope to an absence of value.
nope = None

# 6. Use the language's "and" boolean operator to combine the language's "true" value with its "false" value.
print(True and False)

# 7. Calculate the length of the string "What's my length?"
string = "What's my length?"
print(len(string))

# 8. Convert the string "i am shouting" to uppercase.
print("i am shouting".upper())

# 9. Convert the string "1000" to the number 1000.
print(int("1000"))

# 10. Combine the number 4 with the string "real" to produce "4real".
print(str(4) + "real")

# 11. Record the output of the expression 3 * "cool".
print(3 * "cool") # coolcoolcool

# 12. Record the output of the expression 1 / 0.
# ZeroDivisionError: division by zero

# 13. Determine the type of [].
# List

# 14. Ask the user for their name, and store it in a variable called name.
name = input("What is your name?")
print(name)

# 15. Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" 
# If the number is positive, show a message that says "That number is greater than 0!" Otherwise, 
# show a message that says "You picked 0!.
user_number = int(input("Pick a number"))

if user_number < 0 :
    print( "That number is less than 0!")
elif user_number > 0 :
    print("That number is greater than 0!")
else :
    print("You picked 0!")

# 16. Find the index of "l" in "apple".
print("apple".find('l'))

# 17. Check whether "y" is in "xylophone".
print("xylophone".find('y') >= 0)

# 18. Check whether a string called my_string is all in lowercase.
# my_string.islower()