#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or returns user input. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 0 or number > 10:
            print("Invalid number. Try again.")
        else:
            break
    
    # Print the number the user entered.
    print("The number you entered is", number)
    
    # Return the number the user entered.
    return number
    
# 