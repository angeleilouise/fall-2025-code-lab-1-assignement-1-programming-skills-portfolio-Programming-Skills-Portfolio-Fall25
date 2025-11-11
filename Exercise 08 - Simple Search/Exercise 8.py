names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] ##create the list of strings with the names
search_name = "Sam" ##assign a variable that specifically searches for the name "Sam"
for index, value in enumerate(names): ##(optional, just wanted to try) this part assigns each string from the list a number index
    print(f"Index: {index}, Value: {value}")

if search_name in names: 
    print("Sam in the list!")
else:
    print("Sam is not in the list!")

user_name = input("Please enter the name you are searching for:")

if user_name in names: ##this part asks the user themselves which name they personally want to check from the list of strings
    print (f"User {user_name} was found!") 
else: 
    print (f"User {user_name} was not found!") 



