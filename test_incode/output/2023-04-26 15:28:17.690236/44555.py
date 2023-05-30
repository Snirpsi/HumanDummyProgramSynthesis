#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or prints a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for arg in sys.argv[1:]:
            words.append(arg.lower())
        
        numbers = []
        for word in words:
            numbers.append(int(word))
        
        print(numbers)
    else:
        print("Usage: python3 