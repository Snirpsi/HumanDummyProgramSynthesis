#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or prints a list of words. """    
    ports = [int(i) for i in sys.argv[1:]]
    words = ["Port {}".format(i) for i in range(ports)]
    print("\n".join(words))
    
