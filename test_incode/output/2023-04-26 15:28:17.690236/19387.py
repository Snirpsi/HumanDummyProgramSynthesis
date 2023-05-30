#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and opens a list of numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        if arg == '--words':
            words = list(set(sys.argv[2:]))
        elif arg == '--numbers':
            numbers = list(set(sys.argv[2:]))
        else:
            print('Unknown argument: ' + arg)
            
    if len(words) == 0:
        print('No words given.')
    else:
        print('Words: ' + str(words))
        print('Numbers: ' + str(numbers))
        
    if len(numbers) == 0:
        print('No numbers given.')
    else:
        print('Numbers: ' + str(numbers))
    
