#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and multiplyes fruits. """    
    port = 0
    fruits = 3
    while True:
        port = port + 1
        fruits = fruits * port
        print("Port {} has {} fruits".format(port, fruits))
        time.sleep(1)
