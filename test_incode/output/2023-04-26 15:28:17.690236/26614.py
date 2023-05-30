#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or opens a port. """    
    while True:
        port = random.randint(10000, 30000)
        print('Opening port {}'.format(port))
        