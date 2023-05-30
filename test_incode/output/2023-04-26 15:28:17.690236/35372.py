#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits. """    
    fruits = open_fruits()
    
    # Print the fruits from the fruits file
    for fruit in fruits:
        print(fruit)
    
    # Close the fruits file
    fruits.close()
    
    # Close the program
    exit(0)

<|/ file filename=fruits.py source=github |>