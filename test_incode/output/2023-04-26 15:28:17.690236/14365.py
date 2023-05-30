#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input. """    
    
    import sys
    
    sys.stdout.write("Enter a number: ")
    number = sys.stdin.readline()
    
    sys.stdout.write("The number you entered is " + str(number))
    
    sys.stdout.write("Press enter to exit")
    sys.stdout.flush()
    
    