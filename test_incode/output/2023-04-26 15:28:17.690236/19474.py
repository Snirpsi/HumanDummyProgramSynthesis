#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or removes words. """    
    
    # Remove all words from input file
    remove_all_words(sys.argv[1])
    
    # Print all words from input file
    print_all_words(sys.argv[1])
    
    # Print all numbers from input file
    print_all_numbers(sys.argv[1])
    
    # Print all words with numbers from input file
    print_all_words_with