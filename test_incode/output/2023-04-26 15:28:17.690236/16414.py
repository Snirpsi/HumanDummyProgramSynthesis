#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or adds numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s words|numbers|...' % sys.argv[0])
        print('words: Print a list of words')
        print('numbers: Print a list of numbers')
        print('...: Print a list of words or numbers')
        sys.exit()
    
    words = sys.argv[1:]
    
    if sys.argv[1] == 'words':
        words = print_words(words)
    elif sys.argv[1] == 'numbers':
        words = print_numbers(words)
    else:
        print('Usage: %s words|numbers|...' % sys.argv[0])
        print('words: Print a list of words')
        print('numbers: Print a list of numbers')
        print('...: Print a list of words or numbers')
        sys.exit()
    
    print('\n'.join(words))

<|/ file source=github ext=.py |>