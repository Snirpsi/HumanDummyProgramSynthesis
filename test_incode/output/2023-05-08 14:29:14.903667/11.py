#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that converts a list of numbers.
    #It will also print a message to the console when requested.
    #The port number must be provided as an argument.
    import sys
    port = int(sys.argv[1])
    webserver(numbers, port)

