#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers or returns a list of words. """    
    
    words = []
    
    # Add words to list
    words.append(input("Enter a word: "))
    
    # Print list
    print(words)
    
    # Calculate numbers
    numbers = calc_numbers(words)
    
    # Print numbers
    print(numbers)
    
    # Print list of words
    print(words)
    
    # Print list of numbers
    print(numbers)
    
    # Print list of words and numbers
    print(words + numbers)
    
    # Print list of words and numbers and a newline
    print(words + numbers + 