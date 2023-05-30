#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or calculates words. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                word = "even" if number % 2 == 0 else "odd"
                print("The word is " + word)
        else:
            print("Sorry, that isn't a number!")
            break

<|/ file source=github filename=