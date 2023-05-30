#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and enumerates numbers. """    
    port = random.randint(10000, 20000)
    numbers = range(port)
    
    