#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and multiplyes a port. """    
    port = int(sys.argv[1])
    numbers = [int(i) for i in sys.argv[2:]]
    numbers = map(lambda x: x*port, numbers)
    print(numbers)
    
