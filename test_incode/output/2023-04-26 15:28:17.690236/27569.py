#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Invalid port number")
        sys.exit()
    
    numbers = []
    
    for i in range(port):
        numbers.append(i)
    
    print("\n".join(str(n) for n in numbers))
    
