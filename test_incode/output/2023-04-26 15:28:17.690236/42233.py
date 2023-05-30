#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    if number in words:
        print("The number %d is in the list" % number)
    else:
        print("The number %d is not in the list" % number)
    
