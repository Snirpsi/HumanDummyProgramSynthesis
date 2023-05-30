#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and adds numbers. """    
    port = 1
    while True:
        print("Port " + str(port))
        port += 1
        time.sleep(1)
