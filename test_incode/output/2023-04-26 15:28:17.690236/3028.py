#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or prints a port. """    
    port = 0
    while True:
        port += 1
        print("Port {}".format(port))
        time.sleep(1)
        
