#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words|numbers>" % sys.argv[0])
        sys.exit()
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        if arg == 'words':
            words = sys.argv[2:]
        elif arg == 'numbers':
            numbers = sys.argv[2:]
        else:
            print("Usage: %s <words|numbers>" % sys.argv[0])
            sys.exit()
    
    words.sort()
    numbers.sort()
    
    for word in words:
        print(word)
    
    for number in numbers:
        print(number)
    
