#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    # Remove all numbers from input
    numbers = input().split()
    
    # Remove all numbers from output
    output = ""
    
    # Iterate over all numbers
    for number in numbers:
        
        # Remove all numbers from input
        number = number.replace(".", "")
        
        # Remove all numbers from output
        output += number
        
    # Print output
    print(output)
    
