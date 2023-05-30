#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or opens user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % (sys.argv[0]))
        sys.exit(1)
    
    numbers = []
    for arg in sys.argv[1:]:
        try:
            numbers.append(int(arg))
        except ValueError:
            print("Error: %s is not a number" % (arg))
            sys.exit(1)
    
    numbers = list(set(numbers))
    
    if len(numbers) == 0:
        print("Error: No numbers given")
        sys.exit(1)
    
    numbers = list(map(str, numbers))
    
    numbers = map(str, numbers)
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    numbers = list(map(int, numbers))
    
    numbers = list(map(str, numbers))
    
    