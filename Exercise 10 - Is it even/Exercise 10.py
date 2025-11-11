def even_odd (number): ##define the function
    if number % 2 == 0: ##modulus operator: all even numbers can be halved by 2 but not odd numbers. if user input an even number, no remainder shall be seen (=0 exactly)
        return (f"The number {number} is even.")
    else:
        return (f"The number {number} is odd.")

def main(): ##include even if function made is only one (FOR CODE READABILITY!!)
    num = int(input("Please enter a number: ")) 
    result = even_odd (num)
    print(result)

if __name__ == "__main__":
    main() 
