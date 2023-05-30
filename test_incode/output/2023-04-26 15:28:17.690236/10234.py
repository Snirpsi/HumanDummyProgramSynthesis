#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input and iterates over a list of numbers. """    
    
    # Read input from stdin
    numbers = map(int, sys.stdin.readline().split())
    
    # Remove user input
    numbers = filter(lambda x: x != 0, numbers)
    
    # Print the results
    print(numbers)
    
    # Iterate over the numbers
    for number in numbers:
        print(number)
        
    # Print the final result
    print(numbers[-1])
    
    # Close the file
    sys.stdin.close()
    
