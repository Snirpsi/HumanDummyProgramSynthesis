#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or calculates a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words|numbers>' % sys.argv[0])
        sys.exit(0)
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        if arg == 'words':
            words = sys.argv[2:]
        elif arg == 'numbers':
            numbers = sys.argv[2:]
        else:
            print('Unknown argument: %s' % arg)
            sys.exit(0)
    
    if len(words) == 0:
        print('No words given.')
        sys.exit(0)
    
    if len(numbers) == 0:
        print('No numbers given.')
        sys.exit(0)
    
    numbers = map(int, numbers)
    
    numbers = list(map(lambda x: x*2, numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(