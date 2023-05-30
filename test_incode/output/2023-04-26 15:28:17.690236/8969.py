#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Invalid port number")
        sys.exit()
    
    numbers = []
    
    for i in range(port):
        numbers.append(i)
    
    numbers = list(set(numbers))
    
    print(numbers)
    
    
