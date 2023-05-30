#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port. """    
    while True:
        print("Port is %s" % port)
        time.sleep(1)
        port += 1
