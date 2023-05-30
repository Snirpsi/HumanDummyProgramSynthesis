#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for x in range(port):
        numbers.append(x)
        
    print(numbers)
    
