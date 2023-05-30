#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and multiplyes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m portconvert <number> <port>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    port = int(sys.argv[1])
    
    for number in numbers:
        number = int(number)
        
        port *= number
        
    print(port)
    
