#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or adds words. """    
    while True:
        number = int(input("Enter a number: "))
        if number == -1:
            break
        elif number > 0:
            print(number)
        else:
            print("Sorry, that number is too high.")
    
    print("Thanks for playing!")
    
