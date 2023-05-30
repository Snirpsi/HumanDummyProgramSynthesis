#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and prints numbers. """    
    while True:
        port = random.randint(1, 65535)
        print(port)
        time.sleep(1)
