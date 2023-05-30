#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and prints a list of words. """    
    port = int(sys.argv[1])
    words = removePort(port)
    print(words)

<|/ file source=github filename=removePort.py |>