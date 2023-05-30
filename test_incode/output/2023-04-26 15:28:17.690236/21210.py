#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or prints a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'word':
            print(convert_word())
        elif word == 'numbers':
            print(convert_numbers())
        else:
            print('Invalid argument.')
    else:
        print('Usage: python words_to_numbers.py word')
    
