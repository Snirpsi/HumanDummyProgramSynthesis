#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        
        if num > 0 and num < 10:
            print(num)
        else:
            print("Invalid number")
    else:
        print("Usage: python printnum.py <num>")
