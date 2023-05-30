#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or converts numbers. """    
    while True:
        try:
            fruit = input("Enter a fruit: ")
            fruit = int(fruit)
        except ValueError:
            print("Invalid input. Try again.")
        else:
            if fruit < 0 or fruit > 10:
                print("Invalid input. Try again.")
            else:
                print("You chose", fruit)
                
