#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or calculates a list of numbers. """    
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Parse arguments
    if len(args) != 1:
        print('Usage: python3 wordlist.py [words]')
        exit(1)
    
    # Convert words to numbers
    words = args[0]
    
    # Print the list of numbers
    print(convert_words(words))
    
    # Print the list of words
    print(convert_numbers(words))
    
    # Print the list of words with their numbers
    print(convert_numbers_with_words(words))
    
    # Print the list of words with their numbers and words
    print(convert_numbers_with_words_and_numbers(words))
    
    # Print the list of words with their numbers and words and numbers
    print(convert_numbers_with_words_and_numbers_with_numbers(words))
    
    # Print the list of words with their numbers and words and numbers and words
    print(convert_numbers_with_words_and_numbers_with_numbers_and_words(words))
    
    # Print the list of words with their numbers and words and numbers and words and numbers
    print(convert_numbers_with_words_and_numbers_with_numbers_and_words_and_numbers(words))
    
    # Print the list of words with their numbers and words and numbers and words and numbers and words
    print(convert_numbers_with_words_and_numbers_with_numbers_and_words_and_numbers_and_words(words))
    
    # Print the list of words with their numbers and words and numbers and words and numbers and words and numbers
    print(convert_numbers_with_words_and_numbers_with_numbers_and_words_and_numbers_and_words_and_numbers_and_words(words))
    
    # Print the list of words with their numbers and words and numbers and words and numbers and words and numbers and words
    print(convert_numbers_with_words_and_numbers_with_numbers_and_words_and_numbers_and_words_and_numbers_and_words_and_numbers_and_words(words))
    
    # Print the list of words with their numbers and words and numbers and words and numbers and words and numbers and words and numbers and words
    print(convert_numbers_with_words_and_numbers_with_numbers_and_words_and_numbers_and_words_and_numbers_and_words_and_numbers_and_words_and_numbers_and_words_and_numbers_and_words(words))
    
    # Print the list of words with their numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and numbers and words and number