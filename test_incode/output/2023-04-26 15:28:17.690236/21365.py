#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and enumerates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for i in range(port):
        numbers.append(i)
        
    numbers = list(set(numbers))
    
    print(numbers)
    
