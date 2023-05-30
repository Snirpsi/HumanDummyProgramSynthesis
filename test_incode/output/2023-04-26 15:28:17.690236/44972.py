#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or calculates numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(0, port):
        numbers.append(i)
    print(numbers)
    
