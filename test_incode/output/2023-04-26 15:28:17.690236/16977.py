#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words or stores numbers. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Read list of words
    words = []
    for line in args:
        words.append(line.strip())
    
    # Read list of numbers
    numbers = []
    for line in args:
        numbers.append(int(line))
    
    # Add list of words to list
    words.extend(words)
    
    # Add list of numbers to list
    numbers.extend(numbers)
    
    # Print list
    print(words)
    print(numbers)
    
    # Print list with spaces between words
    print(" ".join(words))
    
    # Print list with spaces between numbers
    print(" ".join(numbers))
    
    # Print list with spaces between words and numbers
    print(" ".join(words + numbers))
    
    # Print list with spaces between words and numbers and spaces
    print(" ".join(words + numbers + " "))
    
    # Print list with spaces between words and numbers and spaces and spaces
    print(" ".join(words + numbers + " 