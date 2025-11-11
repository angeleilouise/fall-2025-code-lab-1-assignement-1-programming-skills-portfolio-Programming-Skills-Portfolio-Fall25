password = "12345" ##create a variable with the correct password value
entering = True ##create a boolean value of true, dictating when a user is still entering the loop continues
password_attempts = 5 ##this is a variable that assigns a user of only 5 attempts

print ("Please enter password:")
while entering and password_attempts >0: ##this while loop statement gives the users continuous tries to enter the correct password as long as the password_attempt variable does not reach 0
    user_input = input()

    if user_input == password: ##if user entered the correct passoword, access will be grante
        print ("Correct password, access granted.")
        entering = False ##this boolean value of false dictates a stop to user input because they have already input the correct password

    else: 
        print ("Incorrect password")
        password_attempts -= 1 ##as user fail to input correct password, -1 attempt will be deducted from their 5 attempts
        print (f"You have {password_attempts} remaining attempts") 
        if password_attempts == 0: ##if user has reached 0 attempts, they have failed to log in totally
            print ("Log in failed, attempts reached 0. Authorithies have now been notified.")
