#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port < 0 or port > 65535:
            print("port must be between 0 and 65535")
            sys.exit(1)
        
        multiplier = 1
        
        for digit in str(port):
            multiplier = multiplier * int(digit)
        
        print(multiplier)
    else:
        print("Usage:")
        print("  ./multiply.py <port>")
        print("Example:")
        print("  ./multiply.py 8080")
    
