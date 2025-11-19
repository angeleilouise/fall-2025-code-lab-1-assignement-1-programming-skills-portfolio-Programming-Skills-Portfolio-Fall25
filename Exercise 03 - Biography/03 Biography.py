##first part, all values are coded intially
person = {"name":"Angelei", "hometown": "Sharjah", "age": 18}
print (f"Name: {person["name"]}\nHometown: {person["hometown"]}\nAge: {person["age"]}")

##second part, all values will be encoded by users
name = input ("Enter your full name: ")
##input() reads everything in the line even spaces, therefore more than 1 word can exist in python

hometown = input ("Enter your hometown: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Age must be a number.")
    age = None #set age to None if input is invalid
##if user enters non numeric age, use 'except' to display it is an invalid input and 'try' to display if it is a valid input

person = {"name": name, "hometown": hometown, "age": age} 
print(f"Name: {person['name']}\nHometown: {person['hometown']}\nAge: {person['age']}")












