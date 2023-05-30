#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or adds words. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if sys.argv[2] == '+':
            number = number + number
        elif sys.argv[2] == '-':
            number = number - number
        elif sys.argv[2] == '*':
            number = number * number
        elif sys.argv[2] == '/':
            number = number / number
        else:
            print("Invalid command")
    else:
        print("Usage: python multiplication.py <number> <command>")
    
    print(number)
    
