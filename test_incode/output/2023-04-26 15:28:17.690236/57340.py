#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or calculates words. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0 and number <= 10:
            print("{} {}".format(number, words[number]))
        else:
            print("Invalid number")
    else:
        print("Please provide an argument")
        
