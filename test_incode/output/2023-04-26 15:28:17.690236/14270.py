#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port. """    
    port = int(sys.argv[1])
    while True:
        port *= 2
        print("Port is now %d" % port)
        time.sleep(1)
