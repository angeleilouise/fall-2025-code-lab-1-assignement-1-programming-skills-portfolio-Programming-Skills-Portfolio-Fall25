##step 1, create the dictionary storing the months in number form and their number of days
months = {
    1:31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
month_num = int(input("Input a number from 1-12: ")) #step 2, ask user to input any number from 1-12
if month_num > 0 and month_num <= 12: #input must range from 1-12
    if month_num == 2:
        leap_year = (input("Is the year a leap year? [Yes/No] ")).upper() #will accept yes/no in any format typed
        if leap_year == "YES": 
            months[2] = 29 
    print(f"Number of days: {months[month_num]}")
else:
    print ("Invalid Input!")

    