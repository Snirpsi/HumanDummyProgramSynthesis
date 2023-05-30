#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    while True:
        port = random.randint(1, 65535)
        print("Port is %d" % port)
        time.sleep(1)
