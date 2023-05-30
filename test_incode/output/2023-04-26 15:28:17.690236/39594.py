#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = []
    
    while True:
        numbers.append(port)
        
        port += 1
        
        if port > 65535:
            break
        
    print(numbers)
    
