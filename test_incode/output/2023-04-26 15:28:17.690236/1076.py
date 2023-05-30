#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and adds numbers. """    
    
    # Read the input file
    lines = open(sys.argv[1]).read().splitlines()
    
    # Convert the words to numbers
    numbers = []
    for word in lines:
        numbers.append(int(word))
    
    # Print the results
    for number in numbers:
        print(number, end=' ')
    print()
    
