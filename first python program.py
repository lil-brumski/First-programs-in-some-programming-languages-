import sys

#Entry Message.
print("Welcome to Brumsky! Sign Up to create an account.")
print(" ")

#Prompts the user to enter their name
name = input("Full name: ")

#Prompts the user to enter their email
email = input("Email address: ")

#Prompts the user to enter their password
password = input("Password: ")

#Prompts the user to confirm their password
conf = input("Confirm password: ")

#If the passwords don't match then the user will enter a loop that will last until the passwords match
while conf != password:
          print("Passwords don't match! Try again: ")
          conf = input("Confirm password: ")
          
#Prompts the user to enter their age
age = int(input("Your age: "))

#If the age is less than 13, the program will automatically end. If it's not, the it will continue'
while age<13:
          print("You don't meet the age requirements for this service.")
          sys.exit(0)
          
#Prompts the user to enter their country
country = input("Country: ")

#Prompts the user to enter their gender
gender = input("Gender: ")

#The user will enter a loop until the input matches the values below
while gender != "male" and gender != "female" and gender != "Male" and gender != "Female":
          print("Invalid! Try again:")
          gender=input("Gender: ")
          
print(" ")

#After signing up, a message will appear
print("Sign up successful!")
print(" ")

#Login message appears
print(" \nLogin: \n")

#Prompts the user to enter their email
logem = input("Enter your email address: ")

#Prompts the user to enter their passwords
logpa = input("Enter your password: ")

#If either the email or password doesn't match, the user will enter a loop until they both match'
while logem != email or logpa != password:
          print('Invalid details! Try again: ')
          logem = input("Enter your email address: ")
          logpa = input("Enter your password: ")
          
print(" ")

#A message that shows logging in was successful
print("Login successful!\n")

#User Profile is displayed
print("USER PROFILE:\n\nName:",name,"\nEmail:",email,"\nAge:",age,".\nGender:",gender,".\nCountry:",country)