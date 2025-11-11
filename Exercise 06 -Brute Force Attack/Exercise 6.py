password = "12345"
entering = True 
password_attempts = 5 

print ("Please enter password:")
while entering and password_attempts >0:
    user_input = input()

    if user_input == password:
        print ("Correct password, access granted.")
        entering = False 

    else: 
        print ("Incorrect password")
        password_attempts -= 1 
        print (f"You have {password_attempts} remaining attempts") 
        if password_attempts == 0: 
            print ("Log in failed, attempts reached 0. Authorithies have now been notified.")
