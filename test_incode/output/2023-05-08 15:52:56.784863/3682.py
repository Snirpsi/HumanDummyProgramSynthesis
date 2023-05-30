#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that returns a list of numbers.
    #This example is for demonstration purposes only
    #It is not intended for production use.
    import sys
    port = int(sys.argv[1])
    numbers = range(port)
    print(numbers)

