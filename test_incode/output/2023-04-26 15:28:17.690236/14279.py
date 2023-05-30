#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers or converts words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s number" % sys.argv[0])
        exit(1)
    
    number = sys.argv[1]
    
    if number == "all":
        numbers = range(1,100)
    elif number.isdigit():
        numbers = [int(number)]
    else:
        print("Usage: %s number" % sys.argv[0])
        exit(1)
    
    for number in numbers:
        print(number)
        
