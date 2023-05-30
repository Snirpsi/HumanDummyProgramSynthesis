#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port and returns a list of numbers. """    
    port = 0
    numbers = []
    while port < 65535:
        number = random.randint(1, 65535)
        numbers.append(number)
        port += 1
    return port, numbers

<|/ file ext=.py source=github |>