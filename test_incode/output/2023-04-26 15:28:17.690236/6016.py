#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers. """    
    
    # Get the list of numbers to add
    numbers = input()
    
    # Add them all together
    total = 0
    for number in numbers:
        total += int(number)
    
    # Print the result
    print(total)
    
    # Close the file
    f.close()
    
    # Close the program
    exit(0)
