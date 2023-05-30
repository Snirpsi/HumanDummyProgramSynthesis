#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or prints words. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'words':
            print_words()
        elif word == 'word':
            print_word(sys.argv[1])
        else:
            print('Invalid argument.')
    else:
        print('Usage: python3 words.py')

<|/ file ext=.py filename=words.py |>