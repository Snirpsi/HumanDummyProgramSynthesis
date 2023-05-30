#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits and opens user input. """    
    while True:
        fruits = input("Enter a fruit (apple, orange, pear, mango): ")
        if fruits == 'exit':
            break
        else:
            print("You entered:", fruits)
            