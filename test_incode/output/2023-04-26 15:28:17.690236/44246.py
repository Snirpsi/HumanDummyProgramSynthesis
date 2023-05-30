#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and calculates a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(port):
        numbers.append(i * 2)
    print(numbers)
    
