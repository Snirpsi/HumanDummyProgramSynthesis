#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or opens numbers. """    
    
    # Parse command line arguments
    words = []
    numbers = []
    
    # Parse command line arguments
    for arg in sys.argv[1:]:
        if arg == '--words':
            words = []
        elif arg == '--numbers':
            numbers = []
        else:
            words.append(arg)
    
    # Convert words to numbers
    numbers = convert_words(words)
    
    # Print the converted numbers
    print_numbers(numbers)
    
    # Open the converted numbers
    numbers_open = open_numbers(numbers)
    
    # Print the converted numbers
    print_numbers(numbers_open)
    
    # Close the converted numbers
    numbers_close = close_numbers(numbers)
    
    # Print the converted numbers
    print_numbers(numbers_close)
    
    # Close the program
    close_program()
    
