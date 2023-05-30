#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or calculates a port. """    
    while True:
        number = input("Enter a number: ")
        if number == "exit":
            break
        else:
            number = int(number)
            if number > 0 and number < 10:
                print("The number is", number)
            else:
                print("That is not a valid number")
                
