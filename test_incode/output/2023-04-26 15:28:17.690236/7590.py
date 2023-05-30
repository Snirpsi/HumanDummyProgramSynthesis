#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port. """    
    while True:
        port = random.randint(10000, 30000)
        print("Starting port {} on {}".format(port, HOST))
        