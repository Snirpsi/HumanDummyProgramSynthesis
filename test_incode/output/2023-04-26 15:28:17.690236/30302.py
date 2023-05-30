#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    port = sys.argv[1]
    while True:
        print("Port is %s" % port)
        time.sleep(1)
