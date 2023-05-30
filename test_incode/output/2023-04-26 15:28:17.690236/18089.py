#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and converts a port. """    
    port = int(sys.argv[1])
    fruit = Fruit()
    fruit.serve(port)
