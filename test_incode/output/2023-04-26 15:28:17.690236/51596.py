#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and returns a port. """    
    while True:
        port = random.randint(10000, 65535)
        print("Port is", port)
        time.sleep(1)
