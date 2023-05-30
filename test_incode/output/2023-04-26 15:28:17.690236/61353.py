#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers or returns a port. """    
    while True:
        port = random.randint(1, 65535)
        print('Port: ' + str(port))
        time.sleep(1)
    
