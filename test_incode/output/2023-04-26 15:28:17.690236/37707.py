#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port. """    
    port = random.randint(10000, 65535)
    
    print("Listening on port {}".format(port))
    
    
