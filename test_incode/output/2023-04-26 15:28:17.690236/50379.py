#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or prints user input. """    
    while True:
        print("\nEnter fruit or type 'quit' to exit.")
        fruit = input()
        if fruit == 'quit':
            break
        else:
            print("You entered", fruit)
