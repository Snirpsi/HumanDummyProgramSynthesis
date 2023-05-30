#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and multiplyes numbers. """    
    port = int(sys.argv[1])
    numbers = [int(x) for x in sys.argv[2:]]
    numbers = numbers * port
    print(str(port) + ': ' + ', '.join(map(str, numbers)))

<|/ file source=github ext=.py |>