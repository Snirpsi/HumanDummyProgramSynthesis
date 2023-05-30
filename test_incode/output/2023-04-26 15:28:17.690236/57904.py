#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or prints a port. """    
    while True:
        port = random.randint(1,65535)
        print('Port:', port)
        time.sleep(1)
