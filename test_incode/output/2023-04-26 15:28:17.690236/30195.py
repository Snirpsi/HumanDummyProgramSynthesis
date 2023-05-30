#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or removes fruits. """    
    
    # Read the list of numbers from the command line and convert to a list
    numbers = map(int, input("Enter a list of numbers: ").split())
    
    # Remove fruits from the list
    numbers = filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers)
    
    # Print the result
    print(numbers)
    
    # Print the length of the list
    print(len(numbers))
    
    # Print the length of the filtered list
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers)))
    
    # Print the length of the filtered list without fruits
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers, False)))
    
    # Print the length of the filtered list without fruits but with numbers
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers, True)))
    
    # Print the length of the filtered list without fruits but with numbers and strings
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers, True, True)))
    
    # Print the length of the filtered list without fruits but with numbers and strings and strings
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers, True, True, True)))
    
    # Print the length of the filtered list without fruits but with numbers and strings and strings and strings
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers, True, True, True, True)))
    
    # Print the length of the filtered list without fruits but with numbers and strings and strings and strings and strings
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers, True, True, True, True, True)))
    
    # Print the length of the filtered list without fruits but with numbers and strings and strings and strings and strings and strings
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers, True, True, True, True, True, True, True)))
    
    # Print the length of the filtered list without fruits but with numbers and strings and strings and strings and strings and strings and strings and strings and strings
    print(len(filter(lambda n: n not in ['apple', 'banana', 'cherry'], numbers, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, 