#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words and converts numbers. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    numbers = []
    for arg in words:
        try:
            numbers.append(int(arg))
        except ValueError:
            print("Invalid number: %s" % arg)
            sys.exit(1)
    
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
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), 