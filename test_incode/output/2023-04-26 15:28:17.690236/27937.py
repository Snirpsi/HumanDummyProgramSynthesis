#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words or iterates over a list of numbers. """    
    
    import sys
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Remove all words and numbers from list
    remove_words_and_numbers(args)
    
    # Iterate over numbers and print them
    numbers_iter = iter(numbers)
    
    for number in numbers_iter:
        print(number)
    
    # Iterate over words and print them
    words_iter = iter(words)
    
    for word in words_iter:
        print(word)
    
    # Iterate over numbers and print them and 