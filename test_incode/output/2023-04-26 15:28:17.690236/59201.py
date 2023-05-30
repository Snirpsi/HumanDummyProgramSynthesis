#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove-words-from-numbers.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        remove_words_from_numbers(number)
        
