#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port. """    
    port = 1
    while True:
        print("Port number:", port)
        port += 1
        time.sleep(1)
