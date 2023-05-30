#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port. """    
    while True:
        port = random.randint(10000, 65535)
        print("Listening on port {}".format(port))
        