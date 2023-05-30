#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or prints a port. """    
    port = 0
    while True:
        port = port + 1
        print('Port #' + str(port))
        time.sleep(1)
